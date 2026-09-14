#!/usr/bin/env swift
import Foundation
import PDFKit
import AppKit

let args = CommandLine.arguments
guard args.count >= 2 else {
    print("Usage: swift render_page.swift <start_page> [end_page]")
    exit(1)
}

let startPage = Int(args[1]) ?? 1
let endPage = args.count >= 3 ? (Int(args[2]) ?? startPage) : startPage

let pdfPath = "Gulistan-ur.pdf"
guard let doc = PDFDocument(url: URL(fileURLWithPath: pdfPath)) else {
    print("Error: Could not open \(pdfPath)")
    exit(1)
}

let fileManager = FileManager.default
try? fileManager.createDirectory(atPath: "pages", withIntermediateDirectories: true)

let total = doc.pageCount
print("PDF has \(total) pages. Rendering pages \(startPage) to \(endPage)...")

for p in startPage...min(endPage, total) {
    guard let page = doc.page(at: p - 1) else { continue }
    let pageRect = page.bounds(for: .mediaBox)
    let scale: CGFloat = 2.0 // ~144 DPI
    let width = Int(pageRect.width * scale)
    let height = Int(pageRect.height * scale)
    let colorSpace = CGColorSpaceCreateDeviceRGB()
    let bitmapInfo = CGImageAlphaInfo.premultipliedLast.rawValue
    guard let context = CGContext(data: nil, width: width, height: height, bitsPerComponent: 8, bytesPerRow: 0, space: colorSpace, bitmapInfo: bitmapInfo) else { continue }
    context.setFillColor(CGColor(red: 1, green: 1, blue: 1, alpha: 1))
    context.fill(CGRect(x: 0, y: 0, width: width, height: height))
    context.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: context)
    guard let cgImage = context.makeImage() else { continue }
    let rep = NSBitmapImageRep(cgImage: cgImage)
    guard let pngData = rep.representation(using: .png, properties: [:]) else { continue }
    let outPath = String(format: "pages/page_%03d.png", p)
    try? pngData.write(to: URL(fileURLWithPath: outPath))
    print("Rendered \(outPath) (\(width)x\(height))")
}
