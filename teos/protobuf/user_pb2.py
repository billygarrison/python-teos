# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: user.proto

from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database

# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from google.protobuf import struct_pb2 as google_dot_protobuf_dot_struct__pb2


DESCRIPTOR = _descriptor.FileDescriptor(
    name="user.proto",
    package="teos.protobuf.protos.v1",
    syntax="proto3",
    serialized_options=None,
    create_key=_descriptor._internal_create_key,
    serialized_pb=b'\n\nuser.proto\x12\x17teos.protobuf.protos.v1\x1a\x1cgoogle/protobuf/struct.proto""\n\x0fRegisterRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t"y\n\x10RegisterResponse\x12\x0f\n\x07user_id\x18\x01 \x01(\t\x12\x17\n\x0f\x61vailable_slots\x18\x02 \x01(\r\x12\x1b\n\x13subscription_expiry\x18\x03 \x01(\r\x12\x1e\n\x16subscription_signature\x18\x04 \x01(\t"!\n\x0eGetUserRequest\x12\x0f\n\x07user_id\x18\x01 \x01(\t"8\n\x0fGetUserResponse\x12%\n\x04user\x18\x01 \x01(\x0b\x32\x17.google.protobuf.Struct"$\n\x10GetUsersResponse\x12\x10\n\x08user_ids\x18\x01 \x03(\tb\x06proto3',
    dependencies=[google_dot_protobuf_dot_struct__pb2.DESCRIPTOR],
)


_REGISTERREQUEST = _descriptor.Descriptor(
    name="RegisterRequest",
    full_name="teos.protobuf.protos.v1.RegisterRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="teos.protobuf.protos.v1.RegisterRequest.user_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=69,
    serialized_end=103,
)


_REGISTERRESPONSE = _descriptor.Descriptor(
    name="RegisterResponse",
    full_name="teos.protobuf.protos.v1.RegisterResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="teos.protobuf.protos.v1.RegisterResponse.user_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="available_slots",
            full_name="teos.protobuf.protos.v1.RegisterResponse.available_slots",
            index=1,
            number=2,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="subscription_expiry",
            full_name="teos.protobuf.protos.v1.RegisterResponse.subscription_expiry",
            index=2,
            number=3,
            type=13,
            cpp_type=3,
            label=1,
            has_default_value=False,
            default_value=0,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
        _descriptor.FieldDescriptor(
            name="subscription_signature",
            full_name="teos.protobuf.protos.v1.RegisterResponse.subscription_signature",
            index=3,
            number=4,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        ),
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=105,
    serialized_end=226,
)


_GETUSERREQUEST = _descriptor.Descriptor(
    name="GetUserRequest",
    full_name="teos.protobuf.protos.v1.GetUserRequest",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_id",
            full_name="teos.protobuf.protos.v1.GetUserRequest.user_id",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=1,
            has_default_value=False,
            default_value=b"".decode("utf-8"),
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=228,
    serialized_end=261,
)


_GETUSERRESPONSE = _descriptor.Descriptor(
    name="GetUserResponse",
    full_name="teos.protobuf.protos.v1.GetUserResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user",
            full_name="teos.protobuf.protos.v1.GetUserResponse.user",
            index=0,
            number=1,
            type=11,
            cpp_type=10,
            label=1,
            has_default_value=False,
            default_value=None,
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=263,
    serialized_end=319,
)


_GETUSERSRESPONSE = _descriptor.Descriptor(
    name="GetUsersResponse",
    full_name="teos.protobuf.protos.v1.GetUsersResponse",
    filename=None,
    file=DESCRIPTOR,
    containing_type=None,
    create_key=_descriptor._internal_create_key,
    fields=[
        _descriptor.FieldDescriptor(
            name="user_ids",
            full_name="teos.protobuf.protos.v1.GetUsersResponse.user_ids",
            index=0,
            number=1,
            type=9,
            cpp_type=9,
            label=3,
            has_default_value=False,
            default_value=[],
            message_type=None,
            enum_type=None,
            containing_type=None,
            is_extension=False,
            extension_scope=None,
            serialized_options=None,
            file=DESCRIPTOR,
            create_key=_descriptor._internal_create_key,
        )
    ],
    extensions=[],
    nested_types=[],
    enum_types=[],
    serialized_options=None,
    is_extendable=False,
    syntax="proto3",
    extension_ranges=[],
    oneofs=[],
    serialized_start=321,
    serialized_end=357,
)

_GETUSERRESPONSE.fields_by_name["user"].message_type = google_dot_protobuf_dot_struct__pb2._STRUCT
DESCRIPTOR.message_types_by_name["RegisterRequest"] = _REGISTERREQUEST
DESCRIPTOR.message_types_by_name["RegisterResponse"] = _REGISTERRESPONSE
DESCRIPTOR.message_types_by_name["GetUserRequest"] = _GETUSERREQUEST
DESCRIPTOR.message_types_by_name["GetUserResponse"] = _GETUSERRESPONSE
DESCRIPTOR.message_types_by_name["GetUsersResponse"] = _GETUSERSRESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

RegisterRequest = _reflection.GeneratedProtocolMessageType(
    "RegisterRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGISTERREQUEST,
        "__module__": "user_pb2"
        # @@protoc_insertion_point(class_scope:teos.protobuf.protos.v1.RegisterRequest)
    },
)
_sym_db.RegisterMessage(RegisterRequest)

RegisterResponse = _reflection.GeneratedProtocolMessageType(
    "RegisterResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _REGISTERRESPONSE,
        "__module__": "user_pb2"
        # @@protoc_insertion_point(class_scope:teos.protobuf.protos.v1.RegisterResponse)
    },
)
_sym_db.RegisterMessage(RegisterResponse)

GetUserRequest = _reflection.GeneratedProtocolMessageType(
    "GetUserRequest",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERREQUEST,
        "__module__": "user_pb2"
        # @@protoc_insertion_point(class_scope:teos.protobuf.protos.v1.GetUserRequest)
    },
)
_sym_db.RegisterMessage(GetUserRequest)

GetUserResponse = _reflection.GeneratedProtocolMessageType(
    "GetUserResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERRESPONSE,
        "__module__": "user_pb2"
        # @@protoc_insertion_point(class_scope:teos.protobuf.protos.v1.GetUserResponse)
    },
)
_sym_db.RegisterMessage(GetUserResponse)

GetUsersResponse = _reflection.GeneratedProtocolMessageType(
    "GetUsersResponse",
    (_message.Message,),
    {
        "DESCRIPTOR": _GETUSERSRESPONSE,
        "__module__": "user_pb2"
        # @@protoc_insertion_point(class_scope:teos.protobuf.protos.v1.GetUsersResponse)
    },
)
_sym_db.RegisterMessage(GetUsersResponse)


# @@protoc_insertion_point(module_scope)