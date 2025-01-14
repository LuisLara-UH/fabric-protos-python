# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: peer/transaction.proto
"""Generated protocol buffer code."""
from google.protobuf.internal import builder as _builder
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from peer import proposal_response_pb2 as peer_dot_proposal__response__pb2
from common import common_pb2 as common_dot_common__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16peer/transaction.proto\x12\x06protos\x1a\x1cpeer/proposal_response.proto\x1a\x13\x63ommon/common.proto\"]\n\x14ProcessedTransaction\x12-\n\x13transactionEnvelope\x18\x01 \x01(\x0b\x32\x10.common.Envelope\x12\x16\n\x0evalidationCode\x18\x02 \x01(\x05\"9\n\x0bTransaction\x12*\n\x07\x61\x63tions\x18\x01 \x03(\x0b\x32\x19.protos.TransactionAction\"4\n\x11TransactionAction\x12\x0e\n\x06header\x18\x01 \x01(\x0c\x12\x0f\n\x07payload\x18\x02 \x01(\x0c\"m\n\x16\x43haincodeActionPayload\x12\"\n\x1a\x63haincode_proposal_payload\x18\x01 \x01(\x0c\x12/\n\x06\x61\x63tion\x18\x02 \x01(\x0b\x32\x1f.protos.ChaincodeEndorsedAction\"g\n\x17\x43haincodeEndorsedAction\x12!\n\x19proposal_response_payload\x18\x01 \x01(\x0c\x12)\n\x0c\x65ndorsements\x18\x02 \x03(\x0b\x32\x13.protos.Endorsement*\xab\x05\n\x10TxValidationCode\x12\t\n\x05VALID\x10\x00\x12\x10\n\x0cNIL_ENVELOPE\x10\x01\x12\x0f\n\x0b\x42\x41\x44_PAYLOAD\x10\x02\x12\x15\n\x11\x42\x41\x44_COMMON_HEADER\x10\x03\x12\x19\n\x15\x42\x41\x44_CREATOR_SIGNATURE\x10\x04\x12 \n\x1cINVALID_ENDORSER_TRANSACTION\x10\x05\x12\x1e\n\x1aINVALID_CONFIG_TRANSACTION\x10\x06\x12\x1a\n\x16UNSUPPORTED_TX_PAYLOAD\x10\x07\x12\x15\n\x11\x42\x41\x44_PROPOSAL_TXID\x10\x08\x12\x12\n\x0e\x44UPLICATE_TXID\x10\t\x12\x1e\n\x1a\x45NDORSEMENT_POLICY_FAILURE\x10\n\x12\x16\n\x12MVCC_READ_CONFLICT\x10\x0b\x12\x19\n\x15PHANTOM_READ_CONFLICT\x10\x0c\x12\x13\n\x0fUNKNOWN_TX_TYPE\x10\r\x12\x1a\n\x16TARGET_CHAIN_NOT_FOUND\x10\x0e\x12\x14\n\x10MARSHAL_TX_ERROR\x10\x0f\x12\x10\n\x0cNIL_TXACTION\x10\x10\x12\x15\n\x11\x45XPIRED_CHAINCODE\x10\x11\x12\x1e\n\x1a\x43HAINCODE_VERSION_CONFLICT\x10\x12\x12\x18\n\x14\x42\x41\x44_HEADER_EXTENSION\x10\x13\x12\x16\n\x12\x42\x41\x44_CHANNEL_HEADER\x10\x14\x12\x18\n\x14\x42\x41\x44_RESPONSE_PAYLOAD\x10\x15\x12\r\n\tBAD_RWSET\x10\x16\x12\x14\n\x10ILLEGAL_WRITESET\x10\x17\x12\x14\n\x10INVALID_WRITESET\x10\x18\x12\x15\n\x11INVALID_CHAINCODE\x10\x19\x12\x12\n\rNOT_VALIDATED\x10\xfe\x01\x12\x19\n\x14INVALID_OTHER_REASON\x10\xff\x01*E\n\x0cMetaDataKeys\x12\x18\n\x14VALIDATION_PARAMETER\x10\x00\x12\x1b\n\x17VALIDATION_PARAMETER_V2\x10\x01\x42\x66\n\"org.hyperledger.fabric.protos.peerB\x12TransactionPackageZ,github.com/hyperledger/fabric-protos-go/peerb\x06proto3')

_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, globals())
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'peer.transaction_pb2', globals())
if _descriptor._USE_C_DESCRIPTORS == False:

  DESCRIPTOR._options = None
  DESCRIPTOR._serialized_options = b'\n\"org.hyperledger.fabric.protos.peerB\022TransactionPackageZ,github.com/hyperledger/fabric-protos-go/peer'
  _TXVALIDATIONCODE._serialized_start=510
  _TXVALIDATIONCODE._serialized_end=1193
  _METADATAKEYS._serialized_start=1195
  _METADATAKEYS._serialized_end=1264
  _PROCESSEDTRANSACTION._serialized_start=85
  _PROCESSEDTRANSACTION._serialized_end=178
  _TRANSACTION._serialized_start=180
  _TRANSACTION._serialized_end=237
  _TRANSACTIONACTION._serialized_start=239
  _TRANSACTIONACTION._serialized_end=291
  _CHAINCODEACTIONPAYLOAD._serialized_start=293
  _CHAINCODEACTIONPAYLOAD._serialized_end=402
  _CHAINCODEENDORSEDACTION._serialized_start=404
  _CHAINCODEENDORSEDACTION._serialized_end=507
# @@protoc_insertion_point(module_scope)
