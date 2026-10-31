import argparse,json
from pathlib import Path
def analyze(policy):
 directives={}
 for part in policy.split(";"):
  bits=part.strip().split()
  if bits:directives[bits[0].lower()]=bits[1:]
 warnings=[]
 for key in ("default-src","script-src","object-src","base-uri","frame-ancestors"):
  if key not in directives:warnings.append("missing "+key)
 for key,values in directives.items():
  if "*" in values:warnings.append("wildcard in "+key)
  if "'unsafe-inline'" in values or "'unsafe-eval'" in values:warnings.append("unsafe source in "+key)
 return {"directives":directives,"warnings":warnings}
def main():
 p=argparse.ArgumentParser();p.add_argument("file");x=p.parse_args();print(json.dumps(analyze(Path(x.file).read_text(encoding="utf-8")),indent=2))
if __name__=="__main__":main()
