# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/chaincode_shim.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from peer import chaincode_event_pb2 as peer_dot_chaincode__event__pb2
from peer import proposal_pb2 as peer_dot_proposal__pb2
from google.protobuf import timestamp_pb2 as google_dot_protobuf_dot_timestamp__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x19peer/chaincode_shim.proto\x12\x06protos\x1a\x1apeer/chaincode_event.proto\x1a\x13peer/proposal.proto\x1a\x1fgoogle/protobuf/timestamp.proto\"\xa9\x05\n\x10\x43haincodeMessage\x12+\n\x04type\x18\x01 \x01(\x0e\x32\x1d.protos.ChaincodeMessage.Type\x12-\n\ttimestamp\x18\x02 \x01(\x0b\x32\x1a.google.protobuf.Timestamp\x12\x0f\n\x07payload\x18\x03 \x01(\x0c\x12\x0c\n\x04txid\x18\x04 \x01(\t\x12(\n\x08proposal\x18\x05 \x01(\x0b\x32\x16.protos.SignedProposal\x12/\n\x0f\x63haincode_event\x18\x06 \x01(\x0b\x32\x16.protos.ChaincodeEvent\x12\x12\n\nchannel_id\x18\x07 \x01(\t\"\xaa\x03\n\x04Type\x12\r\n\tUNDEFINED\x10\x00\x12\x0c\n\x08REGISTER\x10\x01\x12\x0e\n\nREGISTERED\x10\x02\x12\x08\n\x04INIT\x10\x03\x12\t\n\x05READY\x10\x04\x12\x0f\n\x0bTRANSACTION\x10\x05\x12\r\n\tCOMPLETED\x10\x06\x12\t\n\x05\x45RROR\x10\x07\x12\r\n\tGET_STATE\x10\x08\x12\r\n\tPUT_STATE\x10\t\x12\r\n\tDEL_STATE\x10\n\x12\x14\n\x10INVOKE_CHAINCODE\x10\x0b\x12\x0c\n\x08RESPONSE\x10\r\x12\x16\n\x12GET_STATE_BY_RANGE\x10\x0e\x12\x14\n\x10GET_QUERY_RESULT\x10\x0f\x12\x14\n\x10QUERY_STATE_NEXT\x10\x10\x12\x15\n\x11QUERY_STATE_CLOSE\x10\x11\x12\r\n\tKEEPALIVE\x10\x12\x12\x17\n\x13GET_HISTORY_FOR_KEY\x10\x13\x12\x16\n\x12GET_STATE_METADATA\x10\x14\x12\x16\n\x12PUT_STATE_METADATA\x10\x15\x12\x19\n\x15GET_PRIVATE_DATA_HASH\x10\x16\x12\x16\n\x12PURGE_PRIVATE_DATA\x10\x17\"+\n\x08GetState\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\"3\n\x10GetStateMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\":\n\x08PutState\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\x12\x12\n\ncollection\x18\x03 \x01(\t\"\\\n\x10PutStateMetadata\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x03 \x01(\t\x12\'\n\x08metadata\x18\x04 \x01(\x0b\x32\x15.protos.StateMetadata\"+\n\x08\x44\x65lState\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\"4\n\x11PurgePrivateState\x12\x0b\n\x03key\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\"Y\n\x0fGetStateByRange\x12\x10\n\x08startKey\x18\x01 \x01(\t\x12\x0e\n\x06\x65ndKey\x18\x02 \x01(\t\x12\x12\n\ncollection\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\x0c\"E\n\x0eGetQueryResult\x12\r\n\x05query\x18\x01 \x01(\t\x12\x12\n\ncollection\x18\x02 \x01(\t\x12\x10\n\x08metadata\x18\x03 \x01(\x0c\"3\n\rQueryMetadata\x12\x10\n\x08pageSize\x18\x01 \x01(\x05\x12\x10\n\x08\x62ookmark\x18\x02 \x01(\t\"\x1f\n\x10GetHistoryForKey\x12\x0b\n\x03key\x18\x01 \x01(\t\"\x1c\n\x0eQueryStateNext\x12\n\n\x02id\x18\x01 \x01(\t\"\x1d\n\x0fQueryStateClose\x12\n\n\x02id\x18\x01 \x01(\t\"\'\n\x10QueryResultBytes\x12\x13\n\x0bresultBytes\x18\x01 \x01(\x0c\"j\n\rQueryResponse\x12)\n\x07results\x18\x01 \x03(\x0b\x32\x18.protos.QueryResultBytes\x12\x10\n\x08has_more\x18\x02 \x01(\x08\x12\n\n\x02id\x18\x03 \x01(\t\x12\x10\n\x08metadata\x18\x04 \x01(\x0c\"H\n\x15QueryResponseMetadata\x12\x1d\n\x15\x66\x65tched_records_count\x18\x01 \x01(\x05\x12\x10\n\x08\x62ookmark\x18\x02 \x01(\t\"/\n\rStateMetadata\x12\x0f\n\x07metakey\x18\x01 \x01(\t\x12\r\n\x05value\x18\x02 \x01(\x0c\"=\n\x13StateMetadataResult\x12&\n\x07\x65ntries\x18\x01 \x03(\x0b\x32\x15.protos.StateMetadata2V\n\x10\x43haincodeSupport\x12\x42\n\x08Register\x12\x18.protos.ChaincodeMessage\x1a\x18.protos.ChaincodeMessage(\x01\x30\x01\x32N\n\tChaincode\x12\x41\n\x07\x43onnect\x12\x18.protos.ChaincodeMessage\x1a\x18.protos.ChaincodeMessage(\x01\x30\x01\x42R\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer.chaincode_shim_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"org.hyperledger.fabric.protos.peerZ,github.com/hyperledger/fabric-protos-go/peer'
  _CHAINCODEMESSAGE._serialized_start=120
  _CHAINCODEMESSAGE._serialized_end=801
  _CHAINCODEMESSAGE_TYPE._serialized_start=375
  _CHAINCODEMESSAGE_TYPE._serialized_end=801
  _GETSTATE._serialized_start=803
  _GETSTATE._serialized_end=846
  _GETSTATEMETADATA._serialized_start=848
  _GETSTATEMETADATA._serialized_end=899
  _PUTSTATE._serialized_start=901
  _PUTSTATE._serialized_end=959
  _PUTSTATEMETADATA._serialized_start=961
  _PUTSTATEMETADATA._serialized_end=1053
  _DELSTATE._serialized_start=1055
  _DELSTATE._serialized_end=1098
  _PURGEPRIVATESTATE._serialized_start=1100
  _PURGEPRIVATESTATE._serialized_end=1152
  _GETSTATEBYRANGE._serialized_start=1154
  _GETSTATEBYRANGE._serialized_end=1243
  _GETQUERYRESULT._serialized_start=1245
  _GETQUERYRESULT._serialized_end=1314
  _QUERYMETADATA._serialized_start=1316
  _QUERYMETADATA._serialized_end=1367
  _GETHISTORYFORKEY._serialized_start=1369
  _GETHISTORYFORKEY._serialized_end=1400
  _QUERYSTATENEXT._serialized_start=1402
  _QUERYSTATENEXT._serialized_end=1430
  _QUERYSTATECLOSE._serialized_start=1432
  _QUERYSTATECLOSE._serialized_end=1461
  _QUERYRESULTBYTES._serialized_start=1463
  _QUERYRESULTBYTES._serialized_end=1502
  _QUERYRESPONSE._serialized_start=1504
  _QUERYRESPONSE._serialized_end=1610
  _QUERYRESPONSEMETADATA._serialized_start=1612
  _QUERYRESPONSEMETADATA._serialized_end=1684
  _STATEMETADATA._serialized_start=1686
  _STATEMETADATA._serialized_end=1733
  _STATEMETADATARESULT._serialized_start=1735
  _STATEMETADATARESULT._serialized_end=1796
  _CHAINCODESUPPORT._serialized_start=1798
  _CHAINCODESUPPORT._serialized_end=1884
  _CHAINCODE._serialized_start=1886
  _CHAINCODE._serialized_end=1964
# @@protoc_insertion_point(module_scope)
