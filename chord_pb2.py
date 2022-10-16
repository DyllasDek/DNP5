# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: chord.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x0b\x63hord.proto\"\t\n\x07GetInfo\"$\n\x07SaveKey\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x0c\n\x04text\x18\x02 \x01(\t\"\x17\n\x08RemFiKey\x12\x0b\n\x03key\x18\x01 \x01(\t\".\n\x11GetNodeChordReply\x12\n\n\x02id\x18\x01 \x01(\x05\x12\r\n\x05table\x18\x02 \x03(\t\"\x19\n\x08SRFReply\x12\r\n\x05reply\x18\x01 \x01(\t\"\x19\n\tTypeReply\x12\x0c\n\x04type\x18\x01 \x01(\t\"(\n\x08NodeInit\x12\x0e\n\x06ipaddr\x18\x01 \x01(\t\x12\x0c\n\x04port\x18\x02 \x01(\t\"\"\n\tNodeReply\x12\n\n\x02id\x18\x01 \x01(\x05\x12\t\n\x01m\x18\x02 \x01(\x05\"\x14\n\x06NodeId\x12\n\n\x02id\x18\x01 \x01(\x05\")\n\nDeregReply\x12\x0b\n\x03\x61\x63k\x18\x01 \x01(\x08\x12\x0e\n\x06output\x18\x02 \x01(\t\")\n\nTableReply\x12\x0c\n\x04pred\x18\x01 \x01(\x05\x12\r\n\x05table\x18\x02 \x03(\t\"+\n\x08NodePair\x12\x0e\n\x06nodeId\x18\x01 \x01(\x05\x12\x0f\n\x07\x61\x64\x64ress\x18\x02 \x01(\t\">\n\x0b\x46ingerTable\x12\x15\n\x02id\x18\x01 \x03(\x0b\x32\t.NodePair\x12\x18\n\x05pairs\x18\x02 \x03(\x0b\x32\t.NodePair2\xfb\x02\n\rSimpleService\x12*\n\x08GetChord\x12\x08.GetInfo\x1a\x12.GetNodeChordReply0\x01\x12\'\n\x07GetNode\x12\x08.GetInfo\x1a\x12.GetNodeChordReply\x12\x1b\n\x04Save\x12\x08.SaveKey\x1a\t.SRFReply\x12\x1e\n\x06Remove\x12\t.RemFiKey\x1a\t.SRFReply\x12\x1c\n\x04\x46ind\x12\t.RemFiKey\x1a\t.SRFReply\x12\x1f\n\x07GetType\x12\x08.GetInfo\x1a\n.TypeReply\x12%\n\x0cRegisterNode\x12\t.NodeInit\x1a\n.NodeReply\x12&\n\x0e\x44\x65registerNode\x12\x07.NodeId\x1a\x0b.DeregReply\x12\'\n\x0eGetFingerTable\x12\x07.NodeId\x1a\x0c.FingerTable\x12!\n\x0bReloadTable\x12\x08.GetInfo\x1a\x08.GetInfob\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'chord_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  _GETINFO._serialized_start=15
  _GETINFO._serialized_end=24
  _SAVEKEY._serialized_start=26
  _SAVEKEY._serialized_end=62
  _REMFIKEY._serialized_start=64
  _REMFIKEY._serialized_end=87
  _GETNODECHORDREPLY._serialized_start=89
  _GETNODECHORDREPLY._serialized_end=135
  _SRFREPLY._serialized_start=137
  _SRFREPLY._serialized_end=162
  _TYPEREPLY._serialized_start=164
  _TYPEREPLY._serialized_end=189
  _NODEINIT._serialized_start=191
  _NODEINIT._serialized_end=231
  _NODEREPLY._serialized_start=233
  _NODEREPLY._serialized_end=267
  _NODEID._serialized_start=269
  _NODEID._serialized_end=289
  _DEREGREPLY._serialized_start=291
  _DEREGREPLY._serialized_end=332
  _TABLEREPLY._serialized_start=334
  _TABLEREPLY._serialized_end=375
  _NODEPAIR._serialized_start=377
  _NODEPAIR._serialized_end=420
  _FINGERTABLE._serialized_start=422
  _FINGERTABLE._serialized_end=484
  _SIMPLESERVICE._serialized_start=487
  _SIMPLESERVICE._serialized_end=866
# @@protoc_insertion_point(module_scope)
