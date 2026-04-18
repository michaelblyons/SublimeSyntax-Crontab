# Crontab for Sublime Text

![Screenshot of crontab file with syntax highlighting][screenshot]

## Features

- Syntax highlighting for crontab files.
    - Shell syntax highlighting for `cron` commands.
    - Separate syntax highlighter for "system" crontab files.
- Command Palette entry to load your crontab for editing.
- Configurable color-coded underline for `cron` expression parts.
- Completions for `cron` expressions and enums like month names.
- Hover on a `cron` expression for an explanation.
- Comment and uncommenting lines using <kbd>Ctrl</kbd>+<kbd>/</kbd> or <kbd>Cmd</kbd>+<kbd>/</kbd>.
- "Build" system to lint with `crontab -T` (if supported on your machine).

## Installation

1. Run the “Package Control: Install Package” command.
2. Find and install the **Crontab** plugin.
3. Restart Sublime Text.

## Todos

- [ ] Make autocomplete work after `,` and `-`.

## Credits &amp; Acknowledgements

1. [clarkewd][]'s original [Crontab Highlighting Package][clarkewd-cron] which was inherited from [kevinior][] and [WheresWardy][].
2. [Varun Nayyar][nayyarv] and his adaptation of the package to `.sublime-syntax`.
3. Adam Schubert and his [`cron_descriptor`][cron_descriptor] package.

[screenshot]: demo/screenshot.png
[clarkewd]: https://github.com/clarkewd
[clarkewd-cron]: https://github.com/clarkewd/SublimeCrontab
[kevinior]: https://github.com/kevinior
[whereswardy]: https://github.com/WheresWardy
[nayyarv]: https://github.com/nayyarv
[cron_descriptor]: https://github.com/Salamek/cron-descriptor
