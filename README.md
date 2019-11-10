# Crontab for Sublime Text 3

[![GitHub license](https://img.shields.io/github/license/michaelblyons/CrontabSublime.svg)](https://github.com/michaelblyons/CrontabSublime/blob/master/LICENSE) [![GitHub release](https://img.shields.io/github/release/michaelblyons/CrontabSublime.svg)](https://GitHub.com/michaelblyons/CrontabSublime/releases/) [![Package Control](https://packagecontrol.herokuapp.com/downloads/Crontab.svg?style=flat-square)](https://packagecontrol.io/packages/Crontab)

![Example screenshot][screenshot]

## Features

- Syntax highlighting for crontab files (default `*.tab`, `*.crontab` and `cron.d`)
- Color-coded underline for `cron` expressions.
- Completions for `cron` expressions and enums like month names.
- Hover on a `cron` expression for an explanation.
- Shell syntax highlighting for cron commands
- Comment and uncommenting lines using <kbd>Ctrl</kbd>+<kbd>/</kbd> or <kbd>Cmd</kbd>+<kbd>/</kbd>.

## Installation

1. Run “Package Control: Install Package” command
2. Find and Install the `Crontab` plugin.
3. Restart Sublime Text.

## Todos

1. Alert on unescaped usage of `%` in crontab line.
2. Provide a template file of things to do when creating a crontab file.
3. Additional "system" crontab syntax with user/group support.
4. Options to change or disable rainbow underlines.

## Credits/Acknowledgements

1. [clarkewd][]'s original [Crontab Highlighting Package][clarkewd-cron] which was inherited from [kevinior][] and [WheresWardy][]
2. Adam Schubert and his [`cron_descriptor`][cron_descriptor] package.

[screenshot]: CrontabHighlightSample.png
[clarkewd]: https://github.com/clarkewd
[clarkewd-cron]: https://github.com/clarkewd/SublimeCrontab
[kevinior]: https://github.com/kevinior
[whereswardy]: https://github.com/WheresWardy
[cron_descriptor]: https://github.com/Salamek/cron-descriptor
