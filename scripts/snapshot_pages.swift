import Cocoa
import WebKit

let args = CommandLine.arguments
guard args.count >= 2 else {
    print("Usage: swift scripts/snapshot_pages.swift <html_file> [page_ids...]")
    exit(1)
}

let htmlPath = args[1]
let htmlUrl = URL(fileURLWithPath: htmlPath)
let pageIds = args.count > 2 ? Array(args[2...]) : ["page_10", "page_11", "page_12", "page_13", "page_18"]

let app = NSApplication.shared

class Runner: NSObject, WKNavigationDelegate {
    var webView: WKWebView!
    var currentIndex = 0
    let outDir = "snapshots"

    func start() {
        try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)
        let config = WKWebViewConfiguration()
        // Standard viewport size
        webView = WKWebView(frame: CGRect(x: 0, y: 0, width: 940, height: 2200), configuration: config)
        webView.navigationDelegate = self
        webView.loadFileURL(htmlUrl, allowingReadAccessTo: htmlUrl.deletingLastPathComponent())
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        print("Document loaded, waiting for fonts & layout...")
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            self.captureNext()
        }
    }

    func captureNext() {
        guard currentIndex < pageIds.count else {
            print("All snapshots captured successfully!")
            exit(0)
        }
        let pid = pageIds[currentIndex]
        let scrollJs = """
        (function() {
            var el = document.getElementById('\(pid)');
            if (!el) return null;
            el.scrollIntoView({ behavior: 'instant', block: 'start' });
            var r = el.getBoundingClientRect();
            return { x: r.left, y: r.top, w: r.width, h: r.height };
        })();
        """
        webView.evaluateJavaScript(scrollJs) { res, err in
            guard let d = res as? [String: CGFloat],
                  let x = d["x"], let w = d["w"], let h = d["h"], w > 0, h > 0 else {
                print("Could not locate element #\(pid)")
                self.currentIndex += 1
                self.captureNext()
                return
            }

            // Increase viewport height temporarily if needed to cover this page
            let neededHeight = max(2200, h + 80)
            self.webView.frame = CGRect(x: 0, y: 0, width: 940, height: neededHeight)

            DispatchQueue.main.asyncAfter(deadline: .now() + 0.5) {
                // Re-measure after resize
                let remeasureJs = """
                (function() {
                    var el = document.getElementById('\(pid)');
                    el.scrollIntoView({ behavior: 'instant', block: 'start' });
                    var r = el.getBoundingClientRect();
                    return { x: r.left, y: r.top, w: r.width, h: r.height };
                })();
                """
                self.webView.evaluateJavaScript(remeasureJs) { res2, _ in
                    guard let d2 = res2 as? [String: CGFloat],
                          let x2 = d2["x"], let y2 = d2["y"], let w2 = d2["w"], let h2 = d2["h"] else {
                        self.currentIndex += 1
                        self.captureNext()
                        return
                    }

                    let cfg = WKSnapshotConfiguration()
                    cfg.rect = CGRect(x: max(0, x2 - 10), y: max(0, y2 - 4), width: min(940, w2 + 20), height: h2 + 8)
                    self.webView.takeSnapshot(with: cfg) { image, error in
                        if let img = image,
                           let tiff = img.tiffRepresentation,
                           let rep = NSBitmapImageRep(data: tiff),
                           let png = rep.representation(using: .png, properties: [:]) {
                            let outPath = "\(self.outDir)/snapshot_\(pid).png"
                            try? png.write(to: URL(fileURLWithPath: outPath))
                            print("Saved snapshot: \(outPath) (\(Int(w2))x\(Int(h2)))")
                        } else {
                            print("Failed snapshot for \(pid): \(String(describing: error))")
                        }
                        self.currentIndex += 1
                        self.captureNext()
                    }
                }
            }
        }
    }
}

let runner = Runner()
runner.start()
app.run()
