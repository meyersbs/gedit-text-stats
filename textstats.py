"""
A Gedit Plugin for displaying word count, sentence count, ...

Adapted from Wordcount <https://github.com/footley/gedit-wordcount-plugin> Jonathan Butcher <footley@gmail.com>
"""

import re
from gi.repository import GObject, Gtk, Gedit # pylint: disable=E0611

WORD_RE = re.compile(r"[\w-]+")
SENT_RE = re.compile(r"[\w-]+[\.!?]+\s")
CHAR_RE = re.compile(r"[\S]{1}")

def get_text(doc):
    """ Get the document text. """
    start, end = doc.get_bounds()
    return doc.get_text(start, end, False)

class TextstatsPlugin(GObject.Object, Gedit.WindowActivatable):
    """ Plugin """
    __gtype_name__ = "textstats"
    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)
        self._doc_changed_id = None
        self._cc_label = Gtk.Label()
        self._wc_label = Gtk.Label()
        self._sc_label = Gtk.Label()

    def do_activate(self):
        """ This gets called when the plugin is activated. It attaches my labels to the Gedit statusbar and turns them on. """
        self.window.get_statusbar().pack_end(self._cc_label, False, False, 5) # expand=False, fill=False, padding=5
        self.window.get_statusbar().pack_end(self._wc_label, False, False, 5) # expand=False, fill=False, padding=5
        self.window.get_statusbar().pack_end(self._sc_label, False, False, 5) # expand=False, fill=False, padding=5
        self._cc_label.show()
        self._wc_label.show()
        self._sc_label.show()

    def do_deactivate(self):
        """ This gets called when the plugin is activated. It turns off my labels. """
        Gtk.Container.remove(self.window.get_statusbar(), self._cc_label)
        Gtk.Container.remove(self.window.get_statusbar(), self._wc_label)
        Gtk.Container.remove(self.window.get_statusbar(), self._sc_label)
        if self._doc_changed_id:
            self._doc_changed_id[0].disconnect(self._doc_changed_id[1])
        del self._cc_label
        del self._wc_label
        del self._sc_label

    def do_update_state(self):
        """ Updates the state. """
        if self._doc_changed_id:
            self._doc_changed_id[0].disconnect(self._doc_changed_id[1])
        doc = self.window.get_active_document()
        if doc: # If there are open tabs, update the labels
            self._doc_changed_id = (doc, doc.connect("changed", self.on_document_changed))
            self.update_label(doc)
        else:  # If there aren't any open tabs, set the labels to empty strings
            self._cc_label.set_text('')
            self._wc_label.set_text('')
            self._sc_label.set_text('')
    
    def on_document_changed(self, doc):
        """ This gets called when the contents of the document have changed. """
        self.update_label(doc)
        
    def update_label(self, doc):
        """ Update labels. """
        txt = get_text(doc)
        msg = 'CharCount: {0}'.format(len(CHAR_RE.findall(txt)))
        self._cc_label.set_text(msg)
        msg = 'WordCount: {0}'.format(len(WORD_RE.findall(txt)))
        self._wc_label.set_text(msg)
        msg = 'SentCount: {0}'.format(len(SENT_RE.findall(txt)))
        self._sc_label.set_text(msg)

