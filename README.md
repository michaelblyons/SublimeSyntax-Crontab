# Crontab for Sublime Text 3

version 0.2

![Example screenshot](CrontabHighlightSample.png)

A package I wrote for ST3 to syntax highlight Crontabs since [the old package available](https://github.com/clarkewd/SublimeCrontab) has not been updated since 2015 and doesn't work. I have inherited a regex, but intend to remove it's use in a future release as it's quite complicated and doesn't allow TODO 1 easily.

Crontabs are arguably a dying thing with systemd, but crontabs are still a quick and dirty way to get things running without too much effort, so some use is nice.

## Installation

1. Run “Package Control: Install Package” command, find and install `Crontab` plugin.
2. Close and reopen file

## Features

- Will highlight packages with `tab` and `crontab` suffices. For custom suffices/filenames, add to your personal sublime text preferences.
- Uses bash highlighting in your commands.
- Comment and uncommenting lines using <kbd>Ctrl</kbd>+<kbd>/</kbd> or <kbd>Cmd</kbd>+<kbd>/</kbd> works as expected
- Moderately scrupulous highlighting of time strings. (Does not recognize invalid ranges.)
- Highlighting and autocomplete of `@`-strings.

## Todos

1. Investigate bringing back "rainbowed" time strings.
2. Alert on unescaped usage of `%` in crontab line.
3. Provide snippets for inserting new command lines.
4. Provide a template file of things to do when creating a crontab file.
5. Additional "system" crontab syntax with user/group support.

## Credits/Acknowledgements

1. [clarkewd's original Crontab Highlighting Package](https://github.com/clarkewd/SublimeCrontab) which was inherited from [kevinior](https://github.com/kevinior) and [WheresWardy](https://github.com/WheresWardy)

