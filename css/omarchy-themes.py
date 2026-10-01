import re, pathlib
P = pathlib.Path('/home/andres/Documents/i62/.obsidian/plugins/obsidian-advanced-slides')
night = (P/'dist/theme/night.css').read_text()
base = '\n'.join(l for l in night.splitlines() if not l.startswith('@import'))
# cut the :root block out of night; we supply our own
base = re.sub(r':root \{.*?\n\}\n', '', base, count=1, flags=re.S)

THEMES = {
 'tokyo-night':   dict(bg='#1a1b26', surface='#24283b', border='#292e42', text='#c0caf5', code='#a9b1d6', heading='#7aa2f7', accent='#bb9af7', hl='#e0af68', muted='#565f89',
                   kw='#bb9af7', st='#9ece6a', num='#ff9e64', fn='#7aa2f7', cm='#565f89', ty='#0db9d7', at='#f7768e', meta='#449dab'),
 'osaka-jade':    dict(bg='#111c18', surface='#23372B', border='#32473B', text='#D6D5BC', code='#C1C497', heading='#2DD5B7', accent='#E5C736', hl='#D2689C', muted='#53685B',
                   kw='#D2689C', st='#63b07a', num='#E5C736', fn='#2DD5B7', cm='#6f8a78', ty='#8CD3CB', at='#ACD4CF', meta='#a2734b'),
 'matte-black':   dict(bg='#121212', surface='#1e1e1e', border='#2a2a2a', text='#bebebe', code='#bebebe', heading='#eaeaea', accent='#e68e0d', hl='#FFC107', muted='#8a8a8d',
                   kw='#e68e0d', st='#FFC107', num='#D35F5F', fn='#eaeaea', cm='#666666', ty='#f59e0b', at='#D35F5F', meta='#8a8a8d'),
 'ethereal':      dict(bg='#060B1E', surface='#131a3a', border='#252e56', text='#ffcead', code='#ffcead', heading='#c2c4f0', accent='#7d82d9', hl='#c89dc1', muted='#6d7db6',
                   kw='#c89dc1', st='#92a593', num='#eb8b54', fn='#c2c4f0', cm='#6d7db6', ty='#a3bfd1', at='#E9BB4F', meta='#ED5B5A'),
 'event-horizon': dict(bg='#1C1E26', surface='#2E303E', border='#3a3d4e', text='#CBCED0', code='#CBCED0', heading='#26BBD9', accent='#EE64AC', hl='#29D398', muted='#6F6F70',
                   kw='#EE64AC', st='#FAC29A', num='#F09483', fn='#26BBD9', cm='#6F6F70', ty='#59E1E3', at='#E95678', meta='#29D398'),
}

TPL = """/* Omarchy "{name}" theme for Advanced Slides (generated) */
:root {{
  --o-bg: {bg}; --o-surface: {surface}; --o-border: {border};
  --o-text: {text}; --o-heading: {heading}; --o-accent: {accent};
  --o-hl: {hl}; --o-muted: {muted};
  --r-background-color: var(--o-bg);
  --r-main-font: "JetBrainsMono Nerd Font", "JetBrains Mono", monospace;
  --r-main-font-size: 36px;
  --r-main-color: var(--o-text);
  --r-block-margin: 20px;
  --r-heading-margin: 0 0 24px 0;
  --r-heading-font: "JetBrainsMono Nerd Font", "JetBrains Mono", monospace;
  --r-heading-color: var(--o-heading);
  --r-heading-line-height: 1.15;
  --r-heading-letter-spacing: -0.02em;
  --r-heading-text-transform: none;
  --r-heading-text-shadow: none;
  --r-heading1-font-weight: 800;
  --r-heading2-font-weight: 700;
  --r-heading3-font-weight: 700;
  --r-heading4-font-weight: 600;
  --r-heading5-font-weight: 600;
  --r-heading6-font-weight: 600;
  --r-heading1-text-shadow: none;
  --r-heading1-size: 2.6em;
  --r-heading2-size: 1.7em;
  --r-heading3-size: 1.3em;
  --r-heading4-size: 1em;
  --r-heading5-size: 0.85em;
  --r-heading6-size: 0.7em;
  --r-code-font: "JetBrainsMono Nerd Font", "JetBrains Mono", monospace;
  --r-link-color: var(--o-accent);
  --r-link-color-dark: var(--o-accent);
  --r-link-color-hover: var(--o-hl);
  --r-selection-background-color: var(--o-accent);
  --r-selection-color: var(--o-bg);
}}
{base}
/* ---- Omarchy extras ---- */
.reveal-viewport {{ background: var(--o-bg); }}
.reveal strong, .reveal b {{ color: var(--o-accent); }}
.reveal em {{ color: var(--o-hl); }}
.reveal mark {{ background: var(--o-hl); color: var(--o-bg); padding: 0 0.2em; border-radius: 4px; }}
.reveal small, .reveal figcaption, .reveal .footnotes {{ color: var(--o-muted); }}
.reveal hr {{ border: none; border-top: 2px solid var(--o-border); margin: 1em 0; }}
.reveal li::marker {{ color: var(--o-accent); }}
.reveal .slides a {{ border-bottom: 1px dashed var(--o-accent); }}
.reveal .slides a:hover {{ border-bottom-color: var(--o-hl); }}
.reveal .slide-number a {{ color: var(--o-muted); text-decoration: none; }}

.reveal blockquote {{
  width: 80%; padding: 0.5em 1em; font-style: normal; text-align: left;
  background: var(--o-surface); border-left: 6px solid var(--o-accent);
  border-radius: 6px; box-shadow: none;
}}

.reveal :not(pre) > code {{
  background: var(--o-surface); color: var(--o-hl);
  padding: 0.05em 0.35em; border-radius: 6px; font-size: 0.9em;
}}
.reveal pre {{
  background: var(--o-surface); border: 1px solid var(--o-border);
  border-radius: 10px; box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}}
.reveal pre code, .reveal pre code.hljs {{
  background: transparent; color: {code}; padding: 0.8em 1em; max-height: 520px;
}}

.reveal table {{ border: 1px solid var(--o-border); border-radius: 8px; }}
.reveal table th, .reveal table td {{ border-color: var(--o-border); padding: 0.35em 0.75em; }}
.reveal table th {{ color: var(--o-heading); background: var(--o-surface); border-bottom: 2px solid var(--o-accent); }}
.reveal table tbody tr:nth-child(even) {{ background: color-mix(in srgb, var(--o-surface) 45%, transparent); }}

.reveal .progress {{ color: var(--o-accent); background: var(--o-border); height: 4px; }}
.reveal .slide-number {{ background: transparent; color: var(--o-muted); font-family: var(--r-main-font); font-size: 16px; }}
.reveal .controls {{ color: var(--o-accent) !important; }}

/* ---- syntax highlighting (overrides the chosen highlight theme) ---- */
.reveal .hljs {{ background: transparent; color: {code}; }}
.reveal .hljs-keyword, .reveal .hljs-selector-tag, .reveal .hljs-literal, .reveal .hljs-doctag {{ color: {kw}; }}
.reveal .hljs-string, .reveal .hljs-regexp, .reveal .hljs-addition, .reveal .hljs-template-tag {{ color: {st}; }}
.reveal .hljs-number, .reveal .hljs-symbol, .reveal .hljs-bullet {{ color: {num}; }}
.reveal .hljs-title, .reveal .hljs-section, .reveal .hljs-function .hljs-title, .reveal .hljs-title.function_ {{ color: {fn}; }}
.reveal .hljs-comment, .reveal .hljs-quote {{ color: {cm}; font-style: italic; }}
.reveal .hljs-type, .reveal .hljs-built_in, .reveal .hljs-class .hljs-title, .reveal .hljs-title.class_ {{ color: {ty}; }}
.reveal .hljs-attr, .reveal .hljs-attribute, .reveal .hljs-variable, .reveal .hljs-template-variable, .reveal .hljs-name, .reveal .hljs-property, .reveal .hljs-params {{ color: {at}; }}
.reveal .hljs-meta, .reveal .hljs-selector-id, .reveal .hljs-selector-class, .reveal .hljs-link, .reveal .hljs-deletion {{ color: {meta}; }}
.reveal .hljs-emphasis {{ font-style: italic; }}
.reveal .hljs-strong {{ font-weight: bold; }}
.reveal .hljs-ln-numbers {{ color: var(--o-muted); }}
.reveal .hljs .highlight-line {{ background: color-mix(in srgb, var(--o-accent) 15%, transparent); }}
"""
for name, c in THEMES.items():
    (P/f'css/omarchy-{name}.css').write_text(TPL.format(name=name, base=base, **c))
    print('wrote', f'css/omarchy-{name}.css')

# ---- Neobrutalism (light, thick borders, hard shadows) ----
NB = """/* Neobrutalism theme for Advanced Slides (generated) */
:root {{
  --nb-bg: #FFF4E0; --nb-ink: #000000; --nb-paper: #FFFFFF;
  --nb-yellow: #FFE14D; --nb-pink: #FF6B9D; --nb-blue: #7FB2FF;
  --nb-green: #5CE1A0; --nb-orange: #FF914D;
  --nb-border: 4px solid var(--nb-ink);
  --nb-shadow: 6px 6px 0 var(--nb-ink);
  --r-background-color: var(--nb-bg);
  --r-main-font: "JetBrainsMono Nerd Font", "JetBrains Mono", monospace;
  --r-main-font-size: 36px;
  --r-main-color: #111111;
  --r-block-margin: 22px;
  --r-heading-margin: 0 0 28px 0;
  --r-heading-font: "JetBrainsMono Nerd Font", "JetBrains Mono", monospace;
  --r-heading-color: var(--nb-ink);
  --r-heading-line-height: 1.15;
  --r-heading-letter-spacing: -0.03em;
  --r-heading-text-transform: none;
  --r-heading-text-shadow: none;
  --r-heading1-font-weight: 800;
  --r-heading2-font-weight: 800;
  --r-heading3-font-weight: 800;
  --r-heading4-font-weight: 700;
  --r-heading5-font-weight: 700;
  --r-heading6-font-weight: 700;
  --r-heading1-text-shadow: none;
  --r-heading1-size: 2.4em;
  --r-heading2-size: 1.6em;
  --r-heading3-size: 1.25em;
  --r-heading4-size: 1em;
  --r-heading5-size: 0.85em;
  --r-heading6-size: 0.7em;
  --r-code-font: "JetBrainsMono Nerd Font", "JetBrains Mono", monospace;
  --r-link-color: var(--nb-ink);
  --r-link-color-dark: var(--nb-ink);
  --r-link-color-hover: var(--nb-ink);
  --r-selection-background-color: var(--nb-yellow);
  --r-selection-color: var(--nb-ink);
}}
{base}
/* ---- Neobrutalism extras ---- */
.reveal-viewport {{ background: var(--nb-bg); }}
.reveal h1 {{
  display: block; width: fit-content; margin-left: auto; margin-right: auto; padding: 0.1em 0.4em;
  background: var(--nb-yellow); border: var(--nb-border); box-shadow: 8px 8px 0 var(--nb-ink);
}}
.reveal h2 {{ background: linear-gradient(transparent 62%, var(--nb-pink) 62%, var(--nb-pink) 92%, transparent 92%); display: block; width: fit-content; margin-left: auto; margin-right: auto; }}
.reveal h3 {{ text-decoration: underline; text-decoration-color: var(--nb-blue); text-decoration-thickness: 0.18em; text-underline-offset: 0.12em; }}

.reveal strong, .reveal b {{ background: var(--nb-yellow); padding: 0 0.15em; }}
.reveal em {{ background: var(--nb-blue); padding: 0 0.15em; }}
.reveal mark {{ background: var(--nb-green); color: var(--nb-ink); padding: 0 0.2em; border: 2px solid var(--nb-ink); }}
.reveal small, .reveal figcaption {{ color: #444; }}
.reveal hr {{ border: none; border-top: var(--nb-border); margin: 1em 0; }}
.reveal ul {{ list-style-type: square; }}
.reveal li::marker {{ color: var(--nb-pink); }}

.reveal .slides a {{ color: var(--nb-ink); font-weight: 700; text-decoration: underline; text-decoration-color: var(--nb-blue); text-decoration-thickness: 0.15em; text-underline-offset: 0.12em; }}
.reveal .slides a:hover {{ background: var(--nb-yellow); }}

.reveal blockquote {{
  width: 80%; padding: 0.6em 1em; font-style: normal; text-align: left;
  background: var(--nb-blue); border: var(--nb-border); box-shadow: var(--nb-shadow); border-radius: 0;
}}

.reveal :not(pre) > code {{
  background: var(--nb-paper); color: var(--nb-ink);
  padding: 0.05em 0.35em; border: 2px solid var(--nb-ink); box-shadow: 3px 3px 0 var(--nb-ink); font-size: 0.85em;
}}
.reveal pre {{ background: var(--nb-paper); border: var(--nb-border); box-shadow: 8px 8px 0 var(--nb-ink); border-radius: 0; }}
.reveal pre code, .reveal pre code.hljs {{ background: transparent; color: #111; padding: 0.8em 1em; max-height: 520px; }}

.reveal table {{ border: var(--nb-border); box-shadow: var(--nb-shadow); background: var(--nb-paper); }}
.reveal table th, .reveal table td {{ border: 3px solid var(--nb-ink); padding: 0.35em 0.75em; }}
.reveal table th {{ background: var(--nb-green); color: var(--nb-ink); }}
.reveal table tbody tr:nth-child(even) {{ background: #FFF9EC; }}

.reveal img.nb, .reveal .nb-card {{ border: var(--nb-border); box-shadow: var(--nb-shadow); background: var(--nb-paper); }}

.reveal .progress {{ color: var(--nb-pink); background: var(--nb-ink); height: 8px; }}
.reveal .slide-number {{ background: var(--nb-ink); color: var(--nb-yellow); font-family: var(--r-main-font); font-size: 16px; font-weight: 700; padding: 4px 10px; }}
.reveal .slide-number a {{ color: var(--nb-yellow); text-decoration: none; }}
.reveal .controls {{ color: var(--nb-ink) !important; }}

/* ---- syntax highlighting (light) ---- */
.reveal .hljs {{ background: transparent; color: #111; }}
.reveal .hljs-keyword, .reveal .hljs-selector-tag, .reveal .hljs-literal, .reveal .hljs-doctag {{ color: #D6246E; font-weight: 700; }}
.reveal .hljs-string, .reveal .hljs-regexp, .reveal .hljs-addition, .reveal .hljs-template-tag {{ color: #0E7A2E; }}
.reveal .hljs-number, .reveal .hljs-symbol, .reveal .hljs-bullet {{ color: #C2410C; }}
.reveal .hljs-title, .reveal .hljs-section, .reveal .hljs-function .hljs-title, .reveal .hljs-title.function_ {{ color: #1D4ED8; font-weight: 700; }}
.reveal .hljs-comment, .reveal .hljs-quote {{ color: #6B6B6B; font-style: italic; }}
.reveal .hljs-type, .reveal .hljs-built_in, .reveal .hljs-class .hljs-title, .reveal .hljs-title.class_ {{ color: #7C3AED; }}
.reveal .hljs-attr, .reveal .hljs-attribute, .reveal .hljs-variable, .reveal .hljs-template-variable, .reveal .hljs-name, .reveal .hljs-property, .reveal .hljs-params {{ color: #B91C1C; }}
.reveal .hljs-meta, .reveal .hljs-selector-id, .reveal .hljs-selector-class, .reveal .hljs-link, .reveal .hljs-deletion {{ color: #0369A1; }}
.reveal .hljs-emphasis {{ font-style: italic; }}
.reveal .hljs-strong {{ font-weight: bold; }}
.reveal .hljs .highlight-line {{ background: var(--nb-yellow); }}
"""
(P/'css/neobrutalism.css').write_text(NB.format(base=base))
print('wrote css/neobrutalism.css')
