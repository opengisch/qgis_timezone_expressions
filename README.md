# what

Adds expression functions to handle timezones in QGIS.

This can be used to convert a UTC time to a local time.

Take the field `last_update`, make sure QGIS knows that it's interpreted as 'UTC', convert to `Tbilisi` time.

```
to_timezone(set_timezone("last_update", 'UTC'), 'Asia/Tbilisi')
```

Wikipedia has [a list of timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### `to_timezone(datetime, 'America/Anguilla')`

Converts `datetime` to `timezone`.
This works only if `datetime` already has a timezone set.

### `set_timezone(datetime, 'UTC')`

Sets `timezone` of `datetime`.
This does not do any conversion

### `to_localtime(datetime)`

Converts the provided `datetime` to the local timezone.
This works only if `datetime` already has a timezone set.

### `to_utc(datetime)`

Converts the provided `datetime` to utc.
This works only if `datetime` already has a timezone set.

# dev

Code style is enforced with pre-commit. To use :
```sh
pip install pre-commit
pre-commit install
```
