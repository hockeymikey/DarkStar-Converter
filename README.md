# DarkStar Converter

A tool that converts all UUID based file names to their Minecraft username based ones.  Created to convert from AddStar's branch Multiverse-Inventories of newer UUID based files back to the older username based ones so they could be converted in PerWorldInventories using MV-I 2.5.
# Example:

| New filename      | Old filename                                |
| :-----------      | :-----------                                |
| jomo.json         | ae795aa8-6327-408e-92ab-25c8a59f3ba1.json   |
| Djinnibutt.tar.gz | 3e50893f-4903-402f-b3b8-10158c6ed75b.tar.gz |

# Usage

`convert-old-names.py [-s] [-D] [-f] [-u] [-v] [-t timestamp] [dir]`

```txt

-s
  simulate. don't rename any files
    default: do not simulate

-D
  don't use dashed UUID format
    default: use dashed UUIDs
    Does nothing

-f
  force overwrite existing UUID files
    default: skip existing files

-u
  use uppercase UUIDs
    default: lowercase UUIDs
    does nothing

-v
  be verbose. prints URLs
    default: don't be verbose

<dir>
  directory to convert files in
    default: current directory
```
