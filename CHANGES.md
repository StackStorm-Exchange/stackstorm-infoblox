# Change Log

## 1.1.0

- Added WAPI version variable to config schema
  
## 1.0.0

* Drop Python 2.7 support

## 0.4.1

- Add explicit support for Python 2 and 3

## 0.4.0

- Added an action to create a HOST record for DNS
- Added an action to delete HOST records for DNS
- Added an action to update HOST records for DNS
- Added some parameters to the `get_hostrecord` action to filter the results (This change has backward compatibility)
- Refactored implementation of the `create_object` action for adding an error handler

## 0.3.0

- Added an action to delete specified A records of DNS
- Added an action to delete specified CNAME records of DNS
- Added an action to delete specified authoritative zone object of DNS
- Added an action to update A records of DNS
- Added an action to update CNAME records of DNS
- Added an action to update object (infoblox.update_object)
- Fixed typo of action get_authzone (changed action name from get_authuone to get_authzone)
- Updated returned value format of get_action method from `_ref` to `ref`.

## 0.2.0

- Added an action to add Authoritative Zone for DNS
- Added an action to restart all member services

## 0.1.0

- Initial Release of Infoblox integration
