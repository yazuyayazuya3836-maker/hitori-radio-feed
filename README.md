# ひとり社長ラジオ — Podcast RSS フィード

GitHub Pages でホスティングしている「ひとり社長ラジオ」の配信用リポジトリ。

- **RSSフィード**: https://yazuyayazuya3836-maker.github.io/hitori-radio-feed/feed.xml
- **Spotify（登録済み 2026-08-30）**: https://open.spotify.com/show/0p6jqbhvIrGoloGmMtKN4k
- **Apple Podcasts（登録済み 2026-08-30・公開済み）**: https://podcasts.apple.com/us/podcast/id6806688752 （番組ID 6806688752）
- **Amazon Music / Audible（登録済み 2026-08-30・ACTIVE）**: 管理は podcasters.amazon.com
- YouTube Music のみ未登録（「アカウントが新しすぎる」制限。2026-08-31以降にStudio→ポッドキャスト→RSSフィード送信で再試行）

## 配信の仕組み

```
MP3をepisodes/に置く → episodes.json追記 → build_feed.py → git push
        ↓
GitHub Pages が feed.xml を公開（数分）
        ↓
Spotify等が自動取得（登録済みプラットフォームは以後ぜんぶ自動）
```

**エピソード追加後にSpotify側での操作は一切不要**。フィード更新から数時間以内に自動反映される。

## Spotify初回登録フロー（完了済み・記録用）

1. creators.spotify.com → 右上アバター → 「新しい番組の追加」
2. 「既存の番組の検索」→ Where's your show hosted? → **Somewhere else**
3. フィードURLを貼る → 「正しく入力されているようです」→ 次へ
4. 所有権確認: 8桁コードが **naohiro.toriya@birdy-official.com**（フィードのitunes:owner）に届く → 入力
5. 国=Japan / 言語=Japanese / プロバイダー=その他 / カテゴリー=Business & Technology（Entrepreneurship, Business, Marketing）→ 送信

## 他プラットフォーム（初回だけ登録が必要・以後は自動）

RSSは共通なので、**各サービスに1回フィードURLを登録すれば、以後のエピソードは全部自動配信**される。

- ~~Apple Podcasts~~: 登録済み。管理は podcastsconnect.apple.com（Apple ID=yazuyayazuya3836@gmail.com）
- ~~Amazon Music / Audible~~: 登録済み。※確認メールはGmailのリンク保護が先にトークンを踏んで自動完了することがある（「already claimed」表示=成功）
- **YouTube Music**: YouTube Studioの「ポッドキャスト」タブ → RSS取り込み（既存のひとり社長ラジオchに紐付け可）
- 上記に登録すると Podcast Index 系の小さいアプリ（Overcast, Pocket Casts等）にも波及する

## エピソード追加手順

1. MP3 を `episodes/epXXX.mp3` として置く（1ファイル100MB未満）
2. `episodes.json` の `episodes` 配列にエントリを追記
3. `python3 build_feed.py` で `feed.xml` を再生成
4. `git add -A && git commit -m "epXXX" && git push` → 数分でPages反映、各プラットフォームが自動取得

## 注意

- このリポジトリは **public**（Podcast配信の性質上、音源・フィードは公開）
- カバーアートは `cover.jpg`（3000x3000）
- 連絡先メール（itunes:owner）は episodes.json で管理。Spotify登録時の所有権確認コードはこのメールに届く
