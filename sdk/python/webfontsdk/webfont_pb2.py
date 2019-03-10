# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: webfont.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='webfont.proto',
  package='webfontsdk',
  syntax='proto3',
  serialized_options=_b('\n\020io.webfont.protoB\014WebfontProtoP\001'),
  serialized_pb=_b('\n\rwebfont.proto\x12\nwebfontsdk\" \n\x0e\x46ontInfoRequet\x12\x0e\n\x06\x61pikey\x18\x01 \x01(\t\"t\n\x0e\x46ontInfoResult\x12\x34\n\x05\x66onts\x18\x01 \x03(\x0b\x32%.webfontsdk.FontInfoResult.FontsEntry\x1a,\n\nFontsEntry\x12\x0b\n\x03key\x18\x01 \x01(\r\x12\r\n\x05value\x18\x02 \x01(\x03:\x02\x38\x01\"x\n\x10\x46ontBuildRequest\x12\x0f\n\x07\x66ont_id\x18\x01 \x01(\r\x12\x0c\n\x04text\x18\x02 \x01(\t\x12\x0e\n\x06\x61pikey\x18\x03 \x01(\t\x12\x10\n\x08need_ttf\x18\x04 \x01(\x08\x12\x10\n\x08need_eot\x18\x05 \x01(\x08\x12\x11\n\tneed_woff\x18\x06 \x01(\x08\"C\n\x14MultFontBuildRequest\x12+\n\x05items\x18\x01 \x03(\x0b\x32\x1c.webfontsdk.FontBuildRequest\"\xa4\x01\n\x12\x46ontBuildBufResult\x12\x0f\n\x07\x66ont_id\x18\x01 \x01(\r\x12\x1b\n\x13\x66ont_format_version\x18\x02 \x01(\r\x12\x15\n\rfont_checksum\x18\x03 \x01(\r\x12\x0f\n\x07name_en\x18\x04 \x01(\t\x12\x11\n\tbytes_ttf\x18\x05 \x01(\x0c\x12\x11\n\tbytes_eot\x18\x06 \x01(\x0c\x12\x12\n\nbytes_woff\x18\x07 \x01(\x0c\"G\n\x16MultFontBuildBufResult\x12-\n\x05items\x18\x01 \x03(\x0b\x32\x1e.webfontsdk.FontBuildBufResult2\xf8\x01\n\x07Greeter\x12K\n\tBuildFont\x12\x1c.webfontsdk.FontBuildRequest\x1a\x1e.webfontsdk.FontBuildBufResult\"\x00\x12W\n\rMultBuildFont\x12 .webfontsdk.MultFontBuildRequest\x1a\".webfontsdk.MultFontBuildBufResult\"\x00\x12G\n\x0bGetFontInfo\x12\x1a.webfontsdk.FontInfoRequet\x1a\x1a.webfontsdk.FontInfoResult\"\x00\x42\"\n\x10io.webfont.protoB\x0cWebfontProtoP\x01\x62\x06proto3')
)




_FONTINFOREQUET = _descriptor.Descriptor(
  name='FontInfoRequet',
  full_name='webfontsdk.FontInfoRequet',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='apikey', full_name='webfontsdk.FontInfoRequet.apikey', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=29,
  serialized_end=61,
)


_FONTINFORESULT_FONTSENTRY = _descriptor.Descriptor(
  name='FontsEntry',
  full_name='webfontsdk.FontInfoResult.FontsEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='key', full_name='webfontsdk.FontInfoResult.FontsEntry.key', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='webfontsdk.FontInfoResult.FontsEntry.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=_b('8\001'),
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=135,
  serialized_end=179,
)

_FONTINFORESULT = _descriptor.Descriptor(
  name='FontInfoResult',
  full_name='webfontsdk.FontInfoResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='fonts', full_name='webfontsdk.FontInfoResult.fonts', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[_FONTINFORESULT_FONTSENTRY, ],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=63,
  serialized_end=179,
)


_FONTBUILDREQUEST = _descriptor.Descriptor(
  name='FontBuildRequest',
  full_name='webfontsdk.FontBuildRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='font_id', full_name='webfontsdk.FontBuildRequest.font_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='webfontsdk.FontBuildRequest.text', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='apikey', full_name='webfontsdk.FontBuildRequest.apikey', index=2,
      number=3, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_ttf', full_name='webfontsdk.FontBuildRequest.need_ttf', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_eot', full_name='webfontsdk.FontBuildRequest.need_eot', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='need_woff', full_name='webfontsdk.FontBuildRequest.need_woff', index=5,
      number=6, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=181,
  serialized_end=301,
)


_MULTFONTBUILDREQUEST = _descriptor.Descriptor(
  name='MultFontBuildRequest',
  full_name='webfontsdk.MultFontBuildRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='webfontsdk.MultFontBuildRequest.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=303,
  serialized_end=370,
)


_FONTBUILDBUFRESULT = _descriptor.Descriptor(
  name='FontBuildBufResult',
  full_name='webfontsdk.FontBuildBufResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='font_id', full_name='webfontsdk.FontBuildBufResult.font_id', index=0,
      number=1, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font_format_version', full_name='webfontsdk.FontBuildBufResult.font_format_version', index=1,
      number=2, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='font_checksum', full_name='webfontsdk.FontBuildBufResult.font_checksum', index=2,
      number=3, type=13, cpp_type=3, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='name_en', full_name='webfontsdk.FontBuildBufResult.name_en', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_ttf', full_name='webfontsdk.FontBuildBufResult.bytes_ttf', index=4,
      number=5, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_eot', full_name='webfontsdk.FontBuildBufResult.bytes_eot', index=5,
      number=6, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='bytes_woff', full_name='webfontsdk.FontBuildBufResult.bytes_woff', index=6,
      number=7, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=373,
  serialized_end=537,
)


_MULTFONTBUILDBUFRESULT = _descriptor.Descriptor(
  name='MultFontBuildBufResult',
  full_name='webfontsdk.MultFontBuildBufResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='items', full_name='webfontsdk.MultFontBuildBufResult.items', index=0,
      number=1, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      serialized_options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  serialized_options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=539,
  serialized_end=610,
)

_FONTINFORESULT_FONTSENTRY.containing_type = _FONTINFORESULT
_FONTINFORESULT.fields_by_name['fonts'].message_type = _FONTINFORESULT_FONTSENTRY
_MULTFONTBUILDREQUEST.fields_by_name['items'].message_type = _FONTBUILDREQUEST
_MULTFONTBUILDBUFRESULT.fields_by_name['items'].message_type = _FONTBUILDBUFRESULT
DESCRIPTOR.message_types_by_name['FontInfoRequet'] = _FONTINFOREQUET
DESCRIPTOR.message_types_by_name['FontInfoResult'] = _FONTINFORESULT
DESCRIPTOR.message_types_by_name['FontBuildRequest'] = _FONTBUILDREQUEST
DESCRIPTOR.message_types_by_name['MultFontBuildRequest'] = _MULTFONTBUILDREQUEST
DESCRIPTOR.message_types_by_name['FontBuildBufResult'] = _FONTBUILDBUFRESULT
DESCRIPTOR.message_types_by_name['MultFontBuildBufResult'] = _MULTFONTBUILDBUFRESULT
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FontInfoRequet = _reflection.GeneratedProtocolMessageType('FontInfoRequet', (_message.Message,), dict(
  DESCRIPTOR = _FONTINFOREQUET,
  __module__ = 'webfont_pb2'
  # @@protoc_insertion_point(class_scope:webfontsdk.FontInfoRequet)
  ))
_sym_db.RegisterMessage(FontInfoRequet)

FontInfoResult = _reflection.GeneratedProtocolMessageType('FontInfoResult', (_message.Message,), dict(

  FontsEntry = _reflection.GeneratedProtocolMessageType('FontsEntry', (_message.Message,), dict(
    DESCRIPTOR = _FONTINFORESULT_FONTSENTRY,
    __module__ = 'webfont_pb2'
    # @@protoc_insertion_point(class_scope:webfontsdk.FontInfoResult.FontsEntry)
    ))
  ,
  DESCRIPTOR = _FONTINFORESULT,
  __module__ = 'webfont_pb2'
  # @@protoc_insertion_point(class_scope:webfontsdk.FontInfoResult)
  ))
_sym_db.RegisterMessage(FontInfoResult)
_sym_db.RegisterMessage(FontInfoResult.FontsEntry)

FontBuildRequest = _reflection.GeneratedProtocolMessageType('FontBuildRequest', (_message.Message,), dict(
  DESCRIPTOR = _FONTBUILDREQUEST,
  __module__ = 'webfont_pb2'
  # @@protoc_insertion_point(class_scope:webfontsdk.FontBuildRequest)
  ))
_sym_db.RegisterMessage(FontBuildRequest)

MultFontBuildRequest = _reflection.GeneratedProtocolMessageType('MultFontBuildRequest', (_message.Message,), dict(
  DESCRIPTOR = _MULTFONTBUILDREQUEST,
  __module__ = 'webfont_pb2'
  # @@protoc_insertion_point(class_scope:webfontsdk.MultFontBuildRequest)
  ))
_sym_db.RegisterMessage(MultFontBuildRequest)

FontBuildBufResult = _reflection.GeneratedProtocolMessageType('FontBuildBufResult', (_message.Message,), dict(
  DESCRIPTOR = _FONTBUILDBUFRESULT,
  __module__ = 'webfont_pb2'
  # @@protoc_insertion_point(class_scope:webfontsdk.FontBuildBufResult)
  ))
_sym_db.RegisterMessage(FontBuildBufResult)

MultFontBuildBufResult = _reflection.GeneratedProtocolMessageType('MultFontBuildBufResult', (_message.Message,), dict(
  DESCRIPTOR = _MULTFONTBUILDBUFRESULT,
  __module__ = 'webfont_pb2'
  # @@protoc_insertion_point(class_scope:webfontsdk.MultFontBuildBufResult)
  ))
_sym_db.RegisterMessage(MultFontBuildBufResult)


DESCRIPTOR._options = None
_FONTINFORESULT_FONTSENTRY._options = None

_GREETER = _descriptor.ServiceDescriptor(
  name='Greeter',
  full_name='webfontsdk.Greeter',
  file=DESCRIPTOR,
  index=0,
  serialized_options=None,
  serialized_start=613,
  serialized_end=861,
  methods=[
  _descriptor.MethodDescriptor(
    name='BuildFont',
    full_name='webfontsdk.Greeter.BuildFont',
    index=0,
    containing_service=None,
    input_type=_FONTBUILDREQUEST,
    output_type=_FONTBUILDBUFRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='MultBuildFont',
    full_name='webfontsdk.Greeter.MultBuildFont',
    index=1,
    containing_service=None,
    input_type=_MULTFONTBUILDREQUEST,
    output_type=_MULTFONTBUILDBUFRESULT,
    serialized_options=None,
  ),
  _descriptor.MethodDescriptor(
    name='GetFontInfo',
    full_name='webfontsdk.Greeter.GetFontInfo',
    index=2,
    containing_service=None,
    input_type=_FONTINFOREQUET,
    output_type=_FONTINFORESULT,
    serialized_options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_GREETER)

DESCRIPTOR.services_by_name['Greeter'] = _GREETER

# @@protoc_insertion_point(module_scope)
