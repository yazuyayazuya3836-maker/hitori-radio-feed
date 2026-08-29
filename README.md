# ひとり社長ラジオ — Podcast RSS フィード

GitHub Pages でホスティングしている「ひとり社長ラジオ」の配信用リポジトリ。

- **RSSフィード**: https://yazuyayazuya3836-maker.github.io/hitori-radio-feed/feed.xml
- このURLを Spotify for Creators / Apple Podcasts Connect / Amazon Music に登録すると配信される

## エピソード追加手順

1. MP3 を `episodes/epXXX.mp3` として置く（1ファイル100MB未満）
2. `episodes.json` の `episodes` 配列にエントリを追記
3. `python3 build_feed.py` で `feed.xml` を再生成
4. `git add -A && git commit -m "epXXX" && git push` → 数分でPages反映、各プラットフォームが自動取得

## 注意

- このリポジトリは **public**（Podcast配信の性質上、音源・フィードは公開）
- カバーアートは `cover.jpg`（3000x3000）
- 連絡先メール（itunes:owner）は episodes.json で管理。Spotify登録時の所有権確認コードはこのメールに届く
