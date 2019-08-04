# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564922489.5901558
_enable_loop = True
_template_filename = 'themes/bnw/templates/tag.tmpl'
_template_uri = 'tag.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


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
    return runtime._inherit_from(context, 'list_post.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        subcategories = context.get('subcategories', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        title = context.get('title', UNDEFINED)
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        date_format = context.get('date_format', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        description = context.get('description', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        def extra_head():
            return render_extra_head(context)
        sorted = context.get('sorted', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        parent = context.get('parent', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('            <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
                __M_writer(str(kind))
                __M_writer(' ')
                __M_writer(str(tag))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')" href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('">\n')
        elif generate_rss:
            __M_writer('        <link rel="alternate" type="application/rss+xml" type="application/rss+xml" title="RSS for ')
            __M_writer(str(kind))
            __M_writer(' ')
            __M_writer(str(tag))
            __M_writer('" href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('">\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        subcategories = context.get('subcategories', UNDEFINED)
        len = context.get('len', UNDEFINED)
        translations = context.get('translations', UNDEFINED)
        generate_rss = context.get('generate_rss', UNDEFINED)
        messages = context.get('messages', UNDEFINED)
        def content():
            return render_content(context)
        title = context.get('title', UNDEFINED)
        date_format = context.get('date_format', UNDEFINED)
        sorted = context.get('sorted', UNDEFINED)
        description = context.get('description', UNDEFINED)
        _link = context.get('_link', UNDEFINED)
        kind = context.get('kind', UNDEFINED)
        tag = context.get('tag', UNDEFINED)
        posts = context.get('posts', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\n  <div class="meta-header">\n    <div class="container">\n      <div class="title">\n\t')
        __M_writer(filters.html_escape(str(title)))
        __M_writer('\n      </div>\n    </div>\n  </div>\n\n    <div class="post-meta">\n      <div class="container">\n\t<div class="meta clearfix">\n')
        if len(translations) > 1 and generate_rss:
            for language in sorted(translations):
                __M_writer('                    <a href="')
                __M_writer(str(_link(kind + "_rss", tag, language)))
                __M_writer('" hreflang="')
                __M_writer(str(language))
                __M_writer('" type="application/rss+xml">')
                __M_writer(str(messages('RSS feed', language)))
                __M_writer(' (')
                __M_writer(str(language))
                __M_writer(')</a>&nbsp;\n')
        elif generate_rss:
            __M_writer('                <a href="')
            __M_writer(str(_link(kind + "_rss", tag)))
            __M_writer('" type="application/rss+xml">')
            __M_writer(str(messages('RSS feed')))
            __M_writer('</a>\n')
        __M_writer('\t</div>\n      </div>\n    </div>\n\n    <div class="sub-categories">\n      <div class="container">\n')
        if description:
            __M_writer('        <p>')
            __M_writer(str(description))
            __M_writer('</p>\n')
        if subcategories:
            __M_writer('        ')
            __M_writer(str(messages('Subcategories:')))
            __M_writer('\n        <ul>\n')
            for name, link in subcategories:
                __M_writer('          <li><a href="')
                __M_writer(str(link))
                __M_writer('">')
                __M_writer(str(name))
                __M_writer('</a></li>\n')
            __M_writer('        </ul>\n')
        __M_writer('      </div>\n    </div>\n\n    <div class="main">\n      <div class="container">\n')
        if posts:
            __M_writer('\t<ul class="postlist">\n')
            for post in posts:
                __M_writer('          <li>\n\t    <time class="listdate" datetime="')
                __M_writer(str(post.date.isoformat()))
                __M_writer('" title="')
                __M_writer(str(post.formatted_date(date_format)))
                __M_writer('">')
                __M_writer(str(post.formatted_date('YYYY-MM-dd')))
                __M_writer('</time>\n\t    <a href="')
                __M_writer(str(post.permalink()))
                __M_writer('"\n\t\t class="listtitle">')
                __M_writer(filters.html_escape(str(post.title())))
                __M_writer('</a>\n\t  </li>\n')
            __M_writer('\t</ul>\n')
        __M_writer('      </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/tag.tmpl", "uri": "tag.tmpl", "source_encoding": "utf-8", "line_map": {"27": 0, "50": 2, "55": 13, "60": 70, "66": 4, "80": 4, "81": 5, "82": 5, "83": 6, "84": 7, "85": 8, "86": 8, "87": 8, "88": 8, "89": 8, "90": 8, "91": 8, "92": 8, "93": 8, "94": 10, "95": 11, "96": 11, "97": 11, "98": 11, "99": 11, "100": 11, "101": 11, "107": 16, "126": 16, "127": 20, "128": 20, "129": 28, "130": 29, "131": 30, "132": 30, "133": 30, "134": 30, "135": 30, "136": 30, "137": 30, "138": 30, "139": 30, "140": 32, "141": 33, "142": 33, "143": 33, "144": 33, "145": 33, "146": 35, "147": 41, "148": 42, "149": 42, "150": 42, "151": 44, "152": 45, "153": 45, "154": 45, "155": 47, "156": 48, "157": 48, "158": 48, "159": 48, "160": 48, "161": 50, "162": 52, "163": 57, "164": 58, "165": 59, "166": 60, "167": 61, "168": 61, "169": 61, "170": 61, "171": 61, "172": 61, "173": 62, "174": 62, "175": 63, "176": 63, "177": 66, "178": 68, "184": 178}}
__M_END_METADATA
"""
