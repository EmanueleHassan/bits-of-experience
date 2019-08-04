# -*- coding:utf-8 -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
STOP_RENDERING = runtime.STOP_RENDERING
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1564925970.6108205
_enable_loop = True
_template_filename = 'themes/bnw/templates/post.tmpl'
_template_uri = 'post.tmpl'
_source_encoding = 'utf-8'
_exports = ['extra_head', 'content']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    ns = runtime.TemplateNamespace('zzz', context._clean_inheritance_tokens(), templateuri='zzz_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'zzz')] = ns

    ns = runtime.TemplateNamespace('helper', context._clean_inheritance_tokens(), templateuri='post_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'helper')] = ns

    ns = runtime.TemplateNamespace('comments', context._clean_inheritance_tokens(), templateuri='comments_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'comments')] = ns

    ns = runtime.TemplateNamespace('math', context._clean_inheritance_tokens(), templateuri='math_helper.tmpl', callables=None,  calling_uri=_template_uri)
    context.namespaces[(__name__, 'math')] = ns

def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, 'base.tmpl', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        zzz = _mako_get_namespace(context, 'zzz')
        helper = _mako_get_namespace(context, 'helper')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        def extra_head():
            return render_extra_head(context._locals(__M_locals))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context._locals(__M_locals))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        __M_writer = context.writer()
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n')
        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'extra_head'):
            context['self'].extra_head(**pageargs)
        

        __M_writer('\n\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_extra_head(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        def extra_head():
            return render_extra_head(context)
        math = _mako_get_namespace(context, 'math')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        parent = _import_ns.get('parent', context.get('parent', UNDEFINED))
        helper = _mako_get_namespace(context, 'helper')
        __M_writer = context.writer()
        __M_writer('\n    ')
        __M_writer(str(parent.extra_head()))
        __M_writer('\n')
        if post.meta('keywords'):
            __M_writer('        <meta name="keywords" content="')
            __M_writer(filters.html_escape(str(post.meta('keywords'))))
            __M_writer('">\n')
        __M_writer('    <meta name="author" content="')
        __M_writer(str(post.author()))
        __M_writer('">\n    ')
        __M_writer(str(helper.open_graph_metadata(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.twitter_card_information(post)))
        __M_writer('\n    ')
        __M_writer(str(helper.meta_translations(post)))
        __M_writer('\n    ')
        __M_writer(str(math.math_styles_ifpost(post)))
        __M_writer('\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        _import_ns = {}
        _mako_get_namespace(context, 'zzz')._populate(_import_ns, ['*'])
        _link = _import_ns.get('_link', context.get('_link', UNDEFINED))
        math = _mako_get_namespace(context, 'math')
        post = _import_ns.get('post', context.get('post', UNDEFINED))
        zzz = _mako_get_namespace(context, 'zzz')
        site_has_comments = _import_ns.get('site_has_comments', context.get('site_has_comments', UNDEFINED))
        title = _import_ns.get('title', context.get('title', UNDEFINED))
        comments = _mako_get_namespace(context, 'comments')
        def content():
            return render_content(context)
        __M_writer = context.writer()
        __M_writer('\n')
        if title and not post.meta('hidetitle'):
            __M_writer('    <div class="post-header">\n        <div class="container">\n            <div class="title">\n                ')
            __M_writer(filters.html_escape(str(title)))
            __M_writer('\n            </div>\n        </div>\n    </div>\n')
        __M_writer('\n    <div class="post-meta">\n      <div class="container">\n\t<div class="meta clearfix">\n\t  <div class="authordate">\n\t    <time class="timeago" datetime="')
        __M_writer(str(post.date.isoformat()))
        __M_writer('">')
        __M_writer(str(post.formatted_date('YYYY/MM/dd')))
        __M_writer('</time>\n\t    ')
        __M_writer(str(zzz.html_translations(post)))
        __M_writer('\n\t    ')
        __M_writer(str(zzz.html_sourcelink()))
        __M_writer('\n\t  </div>\n\t  <div class="post-tags">\n')
        for tag in post.tags:
            __M_writer('\t    <div class="tag">\n\t      <a href="')
            __M_writer(str(_link('tag', tag)))
            __M_writer('" rel="tag">')
            __M_writer(str(tag))
            __M_writer('</a>\n\t    </div>\n')
        __M_writer('\t  </div>\n\t</div>\n      </div>\n    </div>\n\n\n    <div id="post-main" class="main">\n        <div class="container">\n        ')
        __M_writer(str(post.text()))
        __M_writer('\n')
        if not post.meta('nocomments') and site_has_comments:
            __M_writer('            ')
            __M_writer(str(comments.comment_form(post.permalink(absolute=True), post.title(), post._base_path)))
            __M_writer('\n')
        __M_writer('        ')
        __M_writer(str(math.math_scripts_ifpost(post)))
        __M_writer('\n        </div>\n    </div>\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "themes/bnw/templates/post.tmpl", "uri": "post.tmpl", "source_encoding": "utf-8", "line_map": {"23": 3, "26": 4, "29": 5, "32": 6, "38": 0, "58": 1, "59": 3, "60": 4, "61": 5, "62": 6, "63": 7, "68": 19, "73": 61, "79": 9, "91": 9, "92": 10, "93": 10, "94": 11, "95": 12, "96": 12, "97": 12, "98": 14, "99": 14, "100": 14, "101": 15, "102": 15, "103": 16, "104": 16, "105": 17, "106": 17, "107": 18, "108": 18, "114": 21, "129": 21, "130": 22, "131": 23, "132": 26, "133": 26, "134": 31, "135": 36, "136": 36, "137": 36, "138": 36, "139": 37, "140": 37, "141": 38, "142": 38, "143": 41, "144": 42, "145": 43, "146": 43, "147": 43, "148": 43, "149": 46, "150": 54, "151": 54, "152": 55, "153": 56, "154": 56, "155": 56, "156": 58, "157": 58, "158": 58, "164": 158}}
__M_END_METADATA
"""
