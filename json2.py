import json
x='{"_class":"hudson.model.FreeStyleBuild","actions":[{"_class":"hudson.model.CauseAction","causes":[{"_class":"hudson.model.Cause$UserIdCause","shortDescription":"Started by user iam","userId":"admin","userName":"iam"}]},{},{}],"artifacts":[],"building":false,"description":null,"displayName":"#40","duration":374,"estimatedDuration":3758,"executor":null,"fullDisplayName":"test #40","id":"40","keepLog":false,"number":40,"queueId":40,"result":"FAILURE","timestamp":1528181185213,"url":"http://localhost:8080/job/test/40/","builtOn":"","changeSet":{"_class":"hudson.scm.EmptyChangeLogSet","items":[],"kind":null},"culprits":[]}'
loaded=json.loads(x)
while True:
 key=input("enter the key : ")
 try:
  print(loaded[key])
 except:
  print("you enter the wrong key")
