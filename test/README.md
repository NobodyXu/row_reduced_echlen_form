# Hwo to write a test for your file?

Assuming your filename is "filename", then open a file called "test_filename" and write:

```python3
def test(m):
    pass
```

where `m` can be considered to be introduced by `import filename as m`.

To access a function `f` inside that file, just type:

```python3
m.f(...)
```
