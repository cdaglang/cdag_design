```
main: adds [1 3] as v1
      applies [with x: maps [v1]]
      outputs [v2]
where
x: sets [*v1] as v1
   adds [10 v1] as v2
   returns [v2]
where
y: ...
where
z: ...
```

``` 
adds [!{integer} 1 2] as v1
sets [!{ref} v1] as v2
sets [!{var} v1] as v2
```
