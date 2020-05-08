import pgzrun

pgzrun.sys.modules['__main__'].__dict__['images'].subpath = ''
pgzrun.sys.modules['__main__'].__dict__['sounds'].subpath = ''
pgzrun.sys.modules['__main__'].__dict__['music']._loader.subpath = ''
