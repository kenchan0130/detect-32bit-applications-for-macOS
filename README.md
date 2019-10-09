# detect-32bit-applications-for-macOS

32-bit applications will not work from macOS Catalina.
Therefore, listing 32bit applications is effective.

## Usage

If you want to execte at local, you can execute following command like:

```sh
$ ./detect_32bit_applications.py
```

And if you want to include system apps, you should change `IGNORE_SYSTEM_APP` of script from `True` to `False` like:

```python
IGNORE_SYSTEM_APP = False
```

### Setup for Jamf Pro

1. Access https://<JAMF_PRO_SERVER_HOST>/computerExtensionAttributes.html
2. Click "New" button
3. Set any name to "DISPLAY NAME"
4. Select "INVENTORY DISPLAY" to your liking
5. Select "Script" to "INPUT TYPE" and set [this scirpt](./detect_32bit_applications.py)
