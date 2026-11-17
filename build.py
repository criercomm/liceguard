import base64,sys
t=open('src/template.html').read()
for k in ['ROBI','NONIT','COMB','SPRAY','LOGO']:
    d=base64.b64encode(open(f'src/img/{k.lower()}.webp','rb').read()).decode()
    t=t.replace('{{'+k+'}}','data:image/webp;base64,'+d)
assert '{{' not in t
open('index.html','w').write(t)
import json,re
for m in re.findall(r'<script type="application/ld\+json">(.*?)</script>',t,re.S): json.loads(m)
print('ok',len(t))
