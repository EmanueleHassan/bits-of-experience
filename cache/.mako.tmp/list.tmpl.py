# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564922489.5799508
_enable_loop = True
_template_filename = 'themes/bnw/templates/list.tmpl'
_template_uri = 'list.tmpl'
_source_encoding = 'utf-8'
_exports = ['content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        title = context.get('title', UNDEFINED)
        items = context.get('items', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n  <div class="meta-header">\n    <div class="container">\n      <div class="title">\n        ')
        __M_writer(str(title))
        __M_writer('\n      </div>\n    </div>\n  </div>\n\n  <div class="main">\n    <div class="container">\n')
        if items:
            __M_writer('    <ul class="postlist">\n')
            for text, link, count in items:
                __M_writer('        <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(text))
                __M_writer('</a>\n')
                if count:
                    __M_writer('        (')
                    __M_writer(str(count))
                    __M_writer(')\n')
            __M_writer('    </ul>\n')
        else:
            __M_writer('    <p>')
            __M_writer(str(messages("Nothing found.")))
            __M_writer('</p>\n')
        __M_writer('\n    </div>\n  </div>\n\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/list.tmpl", "uri": "list.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "37": 2, "42": 31, "48": 4, "57": 4, "58": 8, "59": 8, "60": 15, "61": 16, "62": 17, "63": 18, "64": 18, "65": 18, "66": 18, "67": 18, "68": 19, "69": 20, "70": 20, "71": 20, "72": 23, "73": 24, "74": 25, "75": 25, "76": 25, "77": 27, "83": 77}}
__M_END_METADATA
"""
