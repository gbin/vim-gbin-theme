# -*- coding: utf-8 -*-
"""
    Gbin Colorscheme
    ~~~~~~~~~~~~~~~~

    Converted by Vim Colorscheme Converter
"""
from pygments.style import Style
from pygments.token import Token, Comment, Name, Keyword, Generic, Number, Operator, String

class GbinStyle(Style):

    background_color = '#000000'
    styles = {
        Token:              '#f6f3e8 bg:#000000',
        Comment:            '#7C0000',
        Name.Attribute:     '#FFD2A7',
        Name.Entity:        '#E18964',
        String:             '#A8FF60',
        Name.Tag:           '#6699CC',
        Operator.Word:      '#ffffff',
        Number:             '#FF73FD',
        Name.Function:      '#FFD2A7',
        Generic.Traceback:  '#ffffff bg:#FF6C60 bold',
        Name.Variable:      '#C6C5FE',
        Generic.Subheading: '#f6f3e8 bold',
        Generic.Heading:    '#f6f3e8 bold',
        Keyword.Type:       '#FFFFB6',
        Name.Constant:      '#99CC99',
        Keyword:            '#6699CC',
        Generic.Output:     '#070707 bg:#000000',
    }
