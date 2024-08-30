// Generated by the protocol buffer compiler.  DO NOT EDIT!
// source: general.proto

#ifndef PROTOBUF_general_2eproto__INCLUDED
#define PROTOBUF_general_2eproto__INCLUDED

#include <string>

#include <google/protobuf/stubs/common.h>

#if GOOGLE_PROTOBUF_VERSION < 2005000
#error This file was generated by a newer version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please update
#error your headers.
#endif
#if 2005000 < GOOGLE_PROTOBUF_MIN_PROTOC_VERSION
#error This file was generated by an older version of protoc which is
#error incompatible with your Protocol Buffer headers.  Please
#error regenerate this file with a newer version of protoc.
#endif

#include <google/protobuf/generated_message_util.h>
#include <google/protobuf/message.h>
#include <google/protobuf/repeated_field.h>
#include <google/protobuf/extension_set.h>
#include <google/protobuf/unknown_field_set.h>
// @@protoc_insertion_point(includes)

// Internal implementation detail -- do not call these.
void  protobuf_AddDesc_general_2eproto();
void protobuf_AssignDesc_general_2eproto();
void protobuf_ShutdownFile_general_2eproto();

class Sign;
class Mail;

// ===================================================================

class Sign : public ::google::protobuf::Message {
 public:
  Sign();
  virtual ~Sign();

  Sign(const Sign& from);

  inline Sign& operator=(const Sign& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Sign& default_instance();

  void Swap(Sign* other);

  // implements Message ----------------------------------------------

  Sign* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Sign& from);
  void MergeFrom(const Sign& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // optional int64 userid = 1;
  inline bool has_userid() const;
  inline void clear_userid();
  static const int kUseridFieldNumber = 1;
  inline ::google::protobuf::int64 userid() const;
  inline void set_userid(::google::protobuf::int64 value);

  // optional int32 signtype = 2;
  inline bool has_signtype() const;
  inline void clear_signtype();
  static const int kSigntypeFieldNumber = 2;
  inline ::google::protobuf::int32 signtype() const;
  inline void set_signtype(::google::protobuf::int32 value);

  // optional string date = 3;
  inline bool has_date() const;
  inline void clear_date();
  static const int kDateFieldNumber = 3;
  inline const ::std::string& date() const;
  inline void set_date(const ::std::string& value);
  inline void set_date(const char* value);
  inline void set_date(const char* value, size_t size);
  inline ::std::string* mutable_date();
  inline ::std::string* release_date();
  inline void set_allocated_date(::std::string* date);

  // @@protoc_insertion_point(class_scope:Sign)
 private:
  inline void set_has_userid();
  inline void clear_has_userid();
  inline void set_has_signtype();
  inline void clear_has_signtype();
  inline void set_has_date();
  inline void clear_has_date();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::int64 userid_;
  ::std::string* date_;
  ::google::protobuf::int32 signtype_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(3 + 31) / 32];

  friend void  protobuf_AddDesc_general_2eproto();
  friend void protobuf_AssignDesc_general_2eproto();
  friend void protobuf_ShutdownFile_general_2eproto();

  void InitAsDefaultInstance();
  static Sign* default_instance_;
};
// -------------------------------------------------------------------

class Mail : public ::google::protobuf::Message {
 public:
  Mail();
  virtual ~Mail();

  Mail(const Mail& from);

  inline Mail& operator=(const Mail& from) {
    CopyFrom(from);
    return *this;
  }

  inline const ::google::protobuf::UnknownFieldSet& unknown_fields() const {
    return _unknown_fields_;
  }

  inline ::google::protobuf::UnknownFieldSet* mutable_unknown_fields() {
    return &_unknown_fields_;
  }

  static const ::google::protobuf::Descriptor* descriptor();
  static const Mail& default_instance();

  void Swap(Mail* other);

  // implements Message ----------------------------------------------

  Mail* New() const;
  void CopyFrom(const ::google::protobuf::Message& from);
  void MergeFrom(const ::google::protobuf::Message& from);
  void CopyFrom(const Mail& from);
  void MergeFrom(const Mail& from);
  void Clear();
  bool IsInitialized() const;

  int ByteSize() const;
  bool MergePartialFromCodedStream(
      ::google::protobuf::io::CodedInputStream* input);
  void SerializeWithCachedSizes(
      ::google::protobuf::io::CodedOutputStream* output) const;
  ::google::protobuf::uint8* SerializeWithCachedSizesToArray(::google::protobuf::uint8* output) const;
  int GetCachedSize() const { return _cached_size_; }
  private:
  void SharedCtor();
  void SharedDtor();
  void SetCachedSize(int size) const;
  public:

  ::google::protobuf::Metadata GetMetadata() const;

  // nested types ----------------------------------------------------

  // accessors -------------------------------------------------------

  // repeated int64 userid = 1;
  inline int userid_size() const;
  inline void clear_userid();
  static const int kUseridFieldNumber = 1;
  inline ::google::protobuf::int64 userid(int index) const;
  inline void set_userid(int index, ::google::protobuf::int64 value);
  inline void add_userid(::google::protobuf::int64 value);
  inline const ::google::protobuf::RepeatedField< ::google::protobuf::int64 >&
      userid() const;
  inline ::google::protobuf::RepeatedField< ::google::protobuf::int64 >*
      mutable_userid();

  // optional int32 type = 2;
  inline bool has_type() const;
  inline void clear_type();
  static const int kTypeFieldNumber = 2;
  inline ::google::protobuf::int32 type() const;
  inline void set_type(::google::protobuf::int32 value);

  // optional string title = 3;
  inline bool has_title() const;
  inline void clear_title();
  static const int kTitleFieldNumber = 3;
  inline const ::std::string& title() const;
  inline void set_title(const ::std::string& value);
  inline void set_title(const char* value);
  inline void set_title(const char* value, size_t size);
  inline ::std::string* mutable_title();
  inline ::std::string* release_title();
  inline void set_allocated_title(::std::string* title);

  // optional string context = 4;
  inline bool has_context() const;
  inline void clear_context();
  static const int kContextFieldNumber = 4;
  inline const ::std::string& context() const;
  inline void set_context(const ::std::string& value);
  inline void set_context(const char* value);
  inline void set_context(const char* value, size_t size);
  inline ::std::string* mutable_context();
  inline ::std::string* release_context();
  inline void set_allocated_context(::std::string* context);

  // optional string attach = 5;
  inline bool has_attach() const;
  inline void clear_attach();
  static const int kAttachFieldNumber = 5;
  inline const ::std::string& attach() const;
  inline void set_attach(const ::std::string& value);
  inline void set_attach(const char* value);
  inline void set_attach(const char* value, size_t size);
  inline ::std::string* mutable_attach();
  inline ::std::string* release_attach();
  inline void set_allocated_attach(::std::string* attach);

  // optional int32 hasattach = 6;
  inline bool has_hasattach() const;
  inline void clear_hasattach();
  static const int kHasattachFieldNumber = 6;
  inline ::google::protobuf::int32 hasattach() const;
  inline void set_hasattach(::google::protobuf::int32 value);

  // optional int32 getattach = 7;
  inline bool has_getattach() const;
  inline void clear_getattach();
  static const int kGetattachFieldNumber = 7;
  inline ::google::protobuf::int32 getattach() const;
  inline void set_getattach(::google::protobuf::int32 value);

  // @@protoc_insertion_point(class_scope:Mail)
 private:
  inline void set_has_type();
  inline void clear_has_type();
  inline void set_has_title();
  inline void clear_has_title();
  inline void set_has_context();
  inline void clear_has_context();
  inline void set_has_attach();
  inline void clear_has_attach();
  inline void set_has_hasattach();
  inline void clear_has_hasattach();
  inline void set_has_getattach();
  inline void clear_has_getattach();

  ::google::protobuf::UnknownFieldSet _unknown_fields_;

  ::google::protobuf::RepeatedField< ::google::protobuf::int64 > userid_;
  ::std::string* title_;
  ::std::string* context_;
  ::google::protobuf::int32 type_;
  ::google::protobuf::int32 hasattach_;
  ::std::string* attach_;
  ::google::protobuf::int32 getattach_;

  mutable int _cached_size_;
  ::google::protobuf::uint32 _has_bits_[(7 + 31) / 32];

  friend void  protobuf_AddDesc_general_2eproto();
  friend void protobuf_AssignDesc_general_2eproto();
  friend void protobuf_ShutdownFile_general_2eproto();

  void InitAsDefaultInstance();
  static Mail* default_instance_;
};
// ===================================================================


// ===================================================================

// Sign

// optional int64 userid = 1;
inline bool Sign::has_userid() const {
  return (_has_bits_[0] & 0x00000001u) != 0;
}
inline void Sign::set_has_userid() {
  _has_bits_[0] |= 0x00000001u;
}
inline void Sign::clear_has_userid() {
  _has_bits_[0] &= ~0x00000001u;
}
inline void Sign::clear_userid() {
  userid_ = GOOGLE_LONGLONG(0);
  clear_has_userid();
}
inline ::google::protobuf::int64 Sign::userid() const {
  return userid_;
}
inline void Sign::set_userid(::google::protobuf::int64 value) {
  set_has_userid();
  userid_ = value;
}

// optional int32 signtype = 2;
inline bool Sign::has_signtype() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Sign::set_has_signtype() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Sign::clear_has_signtype() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Sign::clear_signtype() {
  signtype_ = 0;
  clear_has_signtype();
}
inline ::google::protobuf::int32 Sign::signtype() const {
  return signtype_;
}
inline void Sign::set_signtype(::google::protobuf::int32 value) {
  set_has_signtype();
  signtype_ = value;
}

// optional string date = 3;
inline bool Sign::has_date() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Sign::set_has_date() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Sign::clear_has_date() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Sign::clear_date() {
  if (date_ != &::google::protobuf::internal::kEmptyString) {
    date_->clear();
  }
  clear_has_date();
}
inline const ::std::string& Sign::date() const {
  return *date_;
}
inline void Sign::set_date(const ::std::string& value) {
  set_has_date();
  if (date_ == &::google::protobuf::internal::kEmptyString) {
    date_ = new ::std::string;
  }
  date_->assign(value);
}
inline void Sign::set_date(const char* value) {
  set_has_date();
  if (date_ == &::google::protobuf::internal::kEmptyString) {
    date_ = new ::std::string;
  }
  date_->assign(value);
}
inline void Sign::set_date(const char* value, size_t size) {
  set_has_date();
  if (date_ == &::google::protobuf::internal::kEmptyString) {
    date_ = new ::std::string;
  }
  date_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Sign::mutable_date() {
  set_has_date();
  if (date_ == &::google::protobuf::internal::kEmptyString) {
    date_ = new ::std::string;
  }
  return date_;
}
inline ::std::string* Sign::release_date() {
  clear_has_date();
  if (date_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = date_;
    date_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void Sign::set_allocated_date(::std::string* date) {
  if (date_ != &::google::protobuf::internal::kEmptyString) {
    delete date_;
  }
  if (date) {
    set_has_date();
    date_ = date;
  } else {
    clear_has_date();
    date_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// -------------------------------------------------------------------

// Mail

// repeated int64 userid = 1;
inline int Mail::userid_size() const {
  return userid_.size();
}
inline void Mail::clear_userid() {
  userid_.Clear();
}
inline ::google::protobuf::int64 Mail::userid(int index) const {
  return userid_.Get(index);
}
inline void Mail::set_userid(int index, ::google::protobuf::int64 value) {
  userid_.Set(index, value);
}
inline void Mail::add_userid(::google::protobuf::int64 value) {
  userid_.Add(value);
}
inline const ::google::protobuf::RepeatedField< ::google::protobuf::int64 >&
Mail::userid() const {
  return userid_;
}
inline ::google::protobuf::RepeatedField< ::google::protobuf::int64 >*
Mail::mutable_userid() {
  return &userid_;
}

// optional int32 type = 2;
inline bool Mail::has_type() const {
  return (_has_bits_[0] & 0x00000002u) != 0;
}
inline void Mail::set_has_type() {
  _has_bits_[0] |= 0x00000002u;
}
inline void Mail::clear_has_type() {
  _has_bits_[0] &= ~0x00000002u;
}
inline void Mail::clear_type() {
  type_ = 0;
  clear_has_type();
}
inline ::google::protobuf::int32 Mail::type() const {
  return type_;
}
inline void Mail::set_type(::google::protobuf::int32 value) {
  set_has_type();
  type_ = value;
}

// optional string title = 3;
inline bool Mail::has_title() const {
  return (_has_bits_[0] & 0x00000004u) != 0;
}
inline void Mail::set_has_title() {
  _has_bits_[0] |= 0x00000004u;
}
inline void Mail::clear_has_title() {
  _has_bits_[0] &= ~0x00000004u;
}
inline void Mail::clear_title() {
  if (title_ != &::google::protobuf::internal::kEmptyString) {
    title_->clear();
  }
  clear_has_title();
}
inline const ::std::string& Mail::title() const {
  return *title_;
}
inline void Mail::set_title(const ::std::string& value) {
  set_has_title();
  if (title_ == &::google::protobuf::internal::kEmptyString) {
    title_ = new ::std::string;
  }
  title_->assign(value);
}
inline void Mail::set_title(const char* value) {
  set_has_title();
  if (title_ == &::google::protobuf::internal::kEmptyString) {
    title_ = new ::std::string;
  }
  title_->assign(value);
}
inline void Mail::set_title(const char* value, size_t size) {
  set_has_title();
  if (title_ == &::google::protobuf::internal::kEmptyString) {
    title_ = new ::std::string;
  }
  title_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Mail::mutable_title() {
  set_has_title();
  if (title_ == &::google::protobuf::internal::kEmptyString) {
    title_ = new ::std::string;
  }
  return title_;
}
inline ::std::string* Mail::release_title() {
  clear_has_title();
  if (title_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = title_;
    title_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void Mail::set_allocated_title(::std::string* title) {
  if (title_ != &::google::protobuf::internal::kEmptyString) {
    delete title_;
  }
  if (title) {
    set_has_title();
    title_ = title;
  } else {
    clear_has_title();
    title_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// optional string context = 4;
inline bool Mail::has_context() const {
  return (_has_bits_[0] & 0x00000008u) != 0;
}
inline void Mail::set_has_context() {
  _has_bits_[0] |= 0x00000008u;
}
inline void Mail::clear_has_context() {
  _has_bits_[0] &= ~0x00000008u;
}
inline void Mail::clear_context() {
  if (context_ != &::google::protobuf::internal::kEmptyString) {
    context_->clear();
  }
  clear_has_context();
}
inline const ::std::string& Mail::context() const {
  return *context_;
}
inline void Mail::set_context(const ::std::string& value) {
  set_has_context();
  if (context_ == &::google::protobuf::internal::kEmptyString) {
    context_ = new ::std::string;
  }
  context_->assign(value);
}
inline void Mail::set_context(const char* value) {
  set_has_context();
  if (context_ == &::google::protobuf::internal::kEmptyString) {
    context_ = new ::std::string;
  }
  context_->assign(value);
}
inline void Mail::set_context(const char* value, size_t size) {
  set_has_context();
  if (context_ == &::google::protobuf::internal::kEmptyString) {
    context_ = new ::std::string;
  }
  context_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Mail::mutable_context() {
  set_has_context();
  if (context_ == &::google::protobuf::internal::kEmptyString) {
    context_ = new ::std::string;
  }
  return context_;
}
inline ::std::string* Mail::release_context() {
  clear_has_context();
  if (context_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = context_;
    context_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void Mail::set_allocated_context(::std::string* context) {
  if (context_ != &::google::protobuf::internal::kEmptyString) {
    delete context_;
  }
  if (context) {
    set_has_context();
    context_ = context;
  } else {
    clear_has_context();
    context_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// optional string attach = 5;
inline bool Mail::has_attach() const {
  return (_has_bits_[0] & 0x00000010u) != 0;
}
inline void Mail::set_has_attach() {
  _has_bits_[0] |= 0x00000010u;
}
inline void Mail::clear_has_attach() {
  _has_bits_[0] &= ~0x00000010u;
}
inline void Mail::clear_attach() {
  if (attach_ != &::google::protobuf::internal::kEmptyString) {
    attach_->clear();
  }
  clear_has_attach();
}
inline const ::std::string& Mail::attach() const {
  return *attach_;
}
inline void Mail::set_attach(const ::std::string& value) {
  set_has_attach();
  if (attach_ == &::google::protobuf::internal::kEmptyString) {
    attach_ = new ::std::string;
  }
  attach_->assign(value);
}
inline void Mail::set_attach(const char* value) {
  set_has_attach();
  if (attach_ == &::google::protobuf::internal::kEmptyString) {
    attach_ = new ::std::string;
  }
  attach_->assign(value);
}
inline void Mail::set_attach(const char* value, size_t size) {
  set_has_attach();
  if (attach_ == &::google::protobuf::internal::kEmptyString) {
    attach_ = new ::std::string;
  }
  attach_->assign(reinterpret_cast<const char*>(value), size);
}
inline ::std::string* Mail::mutable_attach() {
  set_has_attach();
  if (attach_ == &::google::protobuf::internal::kEmptyString) {
    attach_ = new ::std::string;
  }
  return attach_;
}
inline ::std::string* Mail::release_attach() {
  clear_has_attach();
  if (attach_ == &::google::protobuf::internal::kEmptyString) {
    return NULL;
  } else {
    ::std::string* temp = attach_;
    attach_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
    return temp;
  }
}
inline void Mail::set_allocated_attach(::std::string* attach) {
  if (attach_ != &::google::protobuf::internal::kEmptyString) {
    delete attach_;
  }
  if (attach) {
    set_has_attach();
    attach_ = attach;
  } else {
    clear_has_attach();
    attach_ = const_cast< ::std::string*>(&::google::protobuf::internal::kEmptyString);
  }
}

// optional int32 hasattach = 6;
inline bool Mail::has_hasattach() const {
  return (_has_bits_[0] & 0x00000020u) != 0;
}
inline void Mail::set_has_hasattach() {
  _has_bits_[0] |= 0x00000020u;
}
inline void Mail::clear_has_hasattach() {
  _has_bits_[0] &= ~0x00000020u;
}
inline void Mail::clear_hasattach() {
  hasattach_ = 0;
  clear_has_hasattach();
}
inline ::google::protobuf::int32 Mail::hasattach() const {
  return hasattach_;
}
inline void Mail::set_hasattach(::google::protobuf::int32 value) {
  set_has_hasattach();
  hasattach_ = value;
}

// optional int32 getattach = 7;
inline bool Mail::has_getattach() const {
  return (_has_bits_[0] & 0x00000040u) != 0;
}
inline void Mail::set_has_getattach() {
  _has_bits_[0] |= 0x00000040u;
}
inline void Mail::clear_has_getattach() {
  _has_bits_[0] &= ~0x00000040u;
}
inline void Mail::clear_getattach() {
  getattach_ = 0;
  clear_has_getattach();
}
inline ::google::protobuf::int32 Mail::getattach() const {
  return getattach_;
}
inline void Mail::set_getattach(::google::protobuf::int32 value) {
  set_has_getattach();
  getattach_ = value;
}


// @@protoc_insertion_point(namespace_scope)

#ifndef SWIG
namespace google {
namespace protobuf {


}  // namespace google
}  // namespace protobuf
#endif  // SWIG

// @@protoc_insertion_point(global_scope)

#endif  // PROTOBUF_general_2eproto__INCLUDED
