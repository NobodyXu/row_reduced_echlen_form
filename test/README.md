# How to use the test framework?

The test framework works on a per-file basis. 

For example, suppose you have a file called "filename" under "src/", then you shall create a file called 
"test_filename" under "test/" which contains all the test every function in that file.


# Hwo to write a test for your file?

Assuming your filename is "filename", then open a file called "test_filename" and write:

```python3
def test(m):
    pass
```

where `m` can be used to access the file.

To access a function `f` inside that file, just type:

```python3
m.f(...)
```
