import { cp, mkdir, readFile, writeFile } from "node:fs/promises";
import { pathToFileURL } from "node:url";
import path from "node:path";

const repo = path.resolve(import.meta.dirname, "..");
const project = path.resolve(repo, "..");
const website = path.join(project, "website");
const siteDir = path.join(repo, "history-business-civilization");
await mkdir(siteDir, { recursive: true });
const workerPath = path.join(website, "dist/server/index.js");
const workerUrl = pathToFileURL(workerPath);
workerUrl.searchParams.set("static-export", Date.now().toString());
const { default: worker } = await import(workerUrl.href);
const response = await worker.fetch(
  new Request("http://localhost/", { headers: { accept: "text/html" } }),
  { ASSETS: { fetch: async () => new Response("Not found", { status: 404 }) } },
  { waitUntil() {}, passThroughOnException() {} },
);
if (!response.ok) throw new Error(`render failed: ${response.status}`);
let html = await response.text();
html = html
  .replaceAll('href="/', 'href="./')
  .replaceAll('src="/', 'src="./')
  .replaceAll('content="/og.png"', 'content="https://edwardchina2023-max.github.io/edward/history-business-civilization/og.png"')
  .replace(/<script[\s\S]*?<\/script>/g, "")
  .replace(/<link rel="modulepreload"[^>]*>/g, "");
await writeFile(path.join(siteDir, "index.html"), html, "utf8");
await cp(path.join(website, "dist/client"), siteDir, { recursive: true });

const workspace = path.join(siteDir, "workspace");
await mkdir(workspace, { recursive: true });
for (const name of [
  "01_项目总纲", "02_资料库", "03_人物库", "04_选题库", "05_文章大纲",
  "06_完整样稿", "07_音频脚本", "08_短视频脚本", "09_图文卡片",
  "10_金句库", "12_商业化方案", "13_复盘记录", "14_版权与引用说明",
]) {
  await cp(path.join(project, name), path.join(workspace, name), { recursive: true });
}
for (const name of ["README.md", "内容生产SOP.md", "AI协作分工方案.md", "11_发布计划排期.md"]) {
  await cp(path.join(project, name), path.join(workspace, name));
}
console.log(path.join(siteDir, "index.html"));
