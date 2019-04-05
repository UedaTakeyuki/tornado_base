# tornado_base
A framework of tornado for modularity.

## Purpose
* Modularity  of Tornado Application handler file.
* Reusability of option definition

## Architecture
* **tornado_base**: parse options, read **TB handler**s, compose appropricate tornado App class, then run tornado server.  
* **TB handler**: Application definition module files

## TB handler
**TB handler** is a python module file which is consist of tornado Request handlers or/and tornado Websocket handlers. Each tornado handlers in TB handler are composed to a tornado application handler by/for **tornado_base**.

One of an advantage of TB handler is, tornado handlers on the same TB handler file can share the **same module global**. So, you can gather related tornado handler modules on the same TB handler file to share glovals, and separate non-related tornado handlers into each TB handler files as your necesity.

Also, a each tornado handlers is provided a same global dictionaly variable **tb_grobal** which can share for server global status.

### Structure
