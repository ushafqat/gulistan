import Cocoa
import WebKit

let outDir = "/Users/dijkstra/Developer/Gulistan/snapshots"
try? FileManager.default.createDirectory(atPath: outDir, withIntermediateDirectories: true)

let htmlPath = "/Users/dijkstra/Developer/Gulistan/docs/study.html"
let htmlUrl = URL(fileURLWithPath: htmlPath)

let app = NSApplication.shared

class UISnapshotRunner: NSObject, WKNavigationDelegate {
    var webView: WKWebView!
    var step = 0

    var window: NSWindow!

    func start() {
        let config = WKWebViewConfiguration()
        webView = WKWebView(frame: CGRect(x: 0, y: 0, width: 960, height: 1100), configuration: config)
        window = NSWindow(contentRect: CGRect(x: 0, y: 0, width: 960, height: 1100),
                          styleMask: [.borderless],
                          backing: .buffered,
                          defer: false)
        window.contentView = webView
        window.orderFrontRegardless()
        webView.navigationDelegate = self
        webView.loadFileURL(htmlUrl, allowingReadAccessTo: htmlUrl.deletingLastPathComponent())
    }

    func webView(_ webView: WKWebView, didFinish navigation: WKNavigation!) {
        print("Page loaded, waiting for fonts & layout...")
        let killTransitions = """
        var st = document.createElement('style');
        st.textContent = '* { transition: none !important; animation: none !important; }';
        document.head.appendChild(st);
        """
        webView.evaluateJavaScript(killTransitions, completionHandler: nil)
        DispatchQueue.main.asyncAfter(deadline: .now() + 2.0) {
            self.runNext()
        }
    }

    func saveSnapshot(name: String, completion: @escaping () -> Void) {
        let cfg = WKSnapshotConfiguration()
        webView.takeSnapshot(with: cfg) { image, error in
            if let img = image,
               let tiff = img.tiffRepresentation,
               let rep = NSBitmapImageRep(data: tiff),
               let png = rep.representation(using: .png, properties: [:]) {
                let p = "\(outDir)/\(name).png"
                try? png.write(to: URL(fileURLWithPath: p))
                print("Captured: \(p)")
            } else {
                print("Failed snapshot for \(name): \(String(describing: error))")
            }
            completion()
        }
    }

    func runNext() {
        step += 1
        switch step {
        case 1:
            print("Step 1: Capturing Header & Top view...")
            saveSnapshot(name: "ui_header_top") {
                self.runNext()
            }
        case 2:
            print("Step 2: Opening Settings Drawer...")
            let js = "document.getElementById('settingsOverlay').classList.add('open'); document.getElementById('settingsOverlay').className;"
            webView.evaluateJavaScript(js) { res, err in
                print("Step 2 result:", res, "err:", err)
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                    self.saveSnapshot(name: "ui_settings_drawer") {
                        self.runNext()
                    }
                }
            }
        case 3:
            print("Step 3: Opening ToC Drawer (Sections Tab)...")
            let js = "document.getElementById('settingsOverlay').classList.remove('open'); document.getElementById('tocOverlay').classList.add('open'); document.getElementById('tocOverlay').className;"
            webView.evaluateJavaScript(js) { res, err in
                print("Step 3 result:", res, "err:", err)
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                    self.saveSnapshot(name: "ui_toc_sections") {
                        self.runNext()
                    }
                }
            }
        case 4:
            print("Step 4: Switching ToC to Pages Tab...")
            let jsTab = "var btn = document.querySelector('.toc-tab-btn[data-toc-tab=\"pages\"]'); if (btn) btn.click();"
            webView.evaluateJavaScript(jsTab) { res, err in
                print("Step 4 result:", res, "err:", err)
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                    self.saveSnapshot(name: "ui_toc_pages") {
                        self.runNext()
                    }
                }
            }
        case 5:
            print("Step 5: Testing Mobile viewport...")
            let jsClose = "document.getElementById('tocOverlay').classList.remove('open');"
            webView.evaluateJavaScript(jsClose) { res, err in
                self.webView.frame = CGRect(x: 0, y: 0, width: 390, height: 844)
                DispatchQueue.main.asyncAfter(deadline: .now() + 0.8) {
                    self.saveSnapshot(name: "ui_mobile_header") {
                        print("All UI snapshots successfully completed!")
                        exit(0)
                    }
                }
            }
        default:
            exit(0)
        }
    }
}

let runner = UISnapshotRunner()
runner.start()
app.run()
