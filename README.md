# gedit-text-stats

A plugin for gedit that shows useful text statistics in the status bar.

---
### Statistics

Character Count: `r"[\S]{1}"`

Word Count: `r"[\w-]+"`

Sentence Count: `r"[\w-]+[\.!?]+\s"`

---
### Installation

``` bash
    wget https://raw.githubusercontent.com/meyersbs/gedit-text-stats/master/install.sh
    chmod +x install.sh
    ./install.sh
```
OR
``` bash
    cd ~/.local/share
    mkdir gedit
    cd gedit
    mkdir plugins
    cd plugins
    wget https://raw.githubusercontent.com/meyersbs/gedit-text-stats/master/textstats.plugin
    wget https://raw.githubusercontent.com/meyersbs/gedit-text-stats/master/textstats.py
```
---
<b>Activate:</b> Settings &#x279C; Preferences &#x279C; Plugins &#x279C; <b>&#x2611;</b> Textstats 

<b>Deactivate:</b> Settings &#x279C; Preferences &#x279C; Plugins &#x279C; <b>&#x274F;</b> Textstats

---
### License

[MIT](LICENSE)

### Contact

...
