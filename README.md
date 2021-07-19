# what

Adds expression functions to handle timezones in QGIS.

This can be used to convert a UTC time to a local time.

Take the field `last_update`, make sure QGIS knows that it's interpreted as 'UTC', convert to `Tbilisi` time.

```
to_timezone(set_timezone("last_update", 'UTC'), 'Asia/Tbilisi')
```

Wikipedia has [a list of timezones](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones).

### `to_timezone(time, 'America/Anguilla')`

Converts `time` to `timezone`.
This works only if `time` already has a timezone set.

### `set_timezone(time, 'UTC')`

Sets `timezone` of `time`.
This does not do any conversion

# dev

Code style is enforced with pre-commit. To use :

pip install pre-commit
pre-commit install
