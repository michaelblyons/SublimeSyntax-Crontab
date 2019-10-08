# Crontab for Sublime Text 3

version 1.0

![Example screenshot][screenshot]

A package for ST3 to syntax highlight Crontabs since [the old package][clarkewd-cron] currently available has not been updated since 2015 and doesn't work.

Crontabs are arguably a dying thing with systemd, but crontabs are still a quick and dirty way to get things running without too much effort, so some help is nice.

## Installation

1. Run “Package Control: Install Package” command, find and install the `Crontab` plugin.
2. Close and reopen the file.

## Features

- Syntax highlighting for `.tab` and `.crontab`, with embedded shell syntax for script contents.
- Color-coded underline for `cron` expression parts.
- Completions for `cron` expressions and enums like month names.
- Comment and uncommenting lines using <kbd>Ctrl</kbd>+<kbd>/</kbd> or <kbd>Cmd</kbd>+<kbd>/</kbd>.
- Hover on a `cron` expression for an explanation.

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
