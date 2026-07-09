# Crontab for Sublime Text

[Crontab][] syntax highlighting and helpers for [Sublime Text][st].

This package leniently highlights 5-term crontab formats.
Make sure that your system supports features
like *N*th-weekday-of-month
before saving them to your crontab file.

![Screenshot of crontab file with syntax highlighting][screenshot]


## Features

- Syntax highlighting for crontab files.
    - Shell syntax highlighting for `cron` commands.
    - Separate syntax highlighter for "system" crontab files.
- Command Palette entry to **Edit my crontab file**.
- Configurable color-coded underline for `cron` expression parts.
- Completions for `cron` expressions and enums like month names.
- Hover on a `cron` expression for an explanation.
- Comment and uncomment lines
  using <kbd>Ctrl</kbd>+<kbd>/</kbd> or <kbd>Cmd</kbd>+<kbd>/</kbd>.
- "Build" system to save as your crontab file
  or to lint if supported on your machine.


## Installation

1. Run the “Package Control: Install Package” command.
2. Find and install the **Crontab** plugin.
3. Restart Sublime Text.


## Lineage &amp; Acknowledgements

- The current syntax is mostly the fault of [Michael Lyons][michaelblyons],
  but follows a succession of other handlers:
    + [Varun Nayyar][nayyarv] adapted the package for Sublime Text 3.
    + [clarkewd][] had it before that.
    + And before him, the Sublime Text 2 version was created
      by [Matthew Ward][whereswardy] and [Kevin O'Rourke][kevinior].

- Build system and colored underlines are by [Michael][michaelblyons].

- The text in hover popups comes from [`cron_descriptor`][pypi]
  by [Adam Schubert][salamek].


[crontab]: https://www.man7.org/linux/man-pages/man5/crontab.5.html
[st]: https://www.sublimetext.com
[screenshot]: demo/screenshot.png
[clarkewd]: https://github.com/clarkewd
[kevinior]: https://github.com/kevinior
[whereswardy]: https://github.com/WheresWardy
[nayyarv]: https://github.com/nayyarv
[michaelblyons]: https://github.com/michaelblyons
[salamek]: https://github.com/Salamek
[pypi]: https://pypi.org/project/cron-descriptor/
