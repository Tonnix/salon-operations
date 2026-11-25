from pathlib import Path
import zipfile, hashlib, sys, re
root=Path(__file__).resolve().parents[1]
version=sys.argv[1] if len(sys.argv)>1 else 'draft'
if not re.fullmatch(r'[A-Za-z0-9._-]+',version): raise SystemExit('Invalid version')
out=root/'releases';out.mkdir(exist_ok=True)
p=out/f'salon-v2-{version}.zip'
with zipfile.ZipFile(p,'w',zipfile.ZIP_DEFLATED) as z:
 for folder in ['src','docs','phases','agents','prompts','tests','project','config','scripts']:
  for f in sorted((root/folder).rglob('*')):
   if f.is_file() and not any(x.startswith('.') or x=='__pycache__' for x in f.relative_to(root).parts): z.write(f,f.relative_to(root))
 for name in ['README.md','AGENTS.md','package.json','.gitignore']: z.write(root/name,name)
print(p,hashlib.sha256(p.read_bytes()).hexdigest())
# Review all included files for sensitive content before distributing.
