# JSON_maker
## Make a json file from lumis in a dataset

Adding script to put the lumis from a dataset into a json file.
```
make_json.py
``` 

### Step 1 : Get lumis from DAS
```      
dasgoclient --query "run,lumi dataset=<Dataset Name> > lumis.txt"
```
      
### Step 2 : Run this script
```      
python make_json.py lumis.txt
```

Author : Mangesh Sonawane

Email : mangesh.sonawane@cern.ch
