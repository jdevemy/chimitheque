# -*- coding: utf-8 -*-
# Copyright 2011 - Thomas Bellembois thomas.bellembois@ens-lyon.fr
# Cecill licence, see LICENSE
# $Id
from gluon import current

TEST = u'this is a test'

APPLICATION_ADMINISTRATOR = u'application administrator(s)'

INDEX = u'index'

TRUE = u'true'
FALSE = u'false'

ERROR = u'an error occured'

LOGIN_FORM_SUBMIT = u'login'

SUBMIT = u'submit'
CANCEL = u'cancel'

SAVE = u'save'
UNDO = u'undo'

DELETE = u'delete'

UPLOAD = u'upload'

BACK = u'back'
DISPLAY_BY = u'display by'
ORDER_BY = u'order by'

CHOOSE_SUBMENU_ITEM = u'choose a menu item'

ITEM = u'item'
DELETE_ITEM = u'delete item'
NO_ITEM_SELECTED = u'no item selected'

I_AM_SURE = u'I am sure'

CHECK_ALL = u'check all'

TOO_MANY_RESULT = u'too many results'

CREATED_UPDATED_BY = u'created/updated by'
USED_BY = u'used by'

ORPHAN = u'orphan'

DETAILS = u'details'

STARTING_TASK = u'starting task'
TASK_COMPLETED = u'task completed'

NOT_AUTHORIZED = u'you are not authorized to do this action'

USER = u'user(s)'
ONLINE_USER = u'online user(s)'

PRIVACY_INFO = u'''Warning: this website contains some nominative informations. If you want to access, modify or delete these informations, please contact the webmaster.'''

SEARCH_product_COMMENT = u'use the form below or the quick request menu to search products'

EMAIL_SUBJECT = u'subject'
EMAIL_MESSAGE = u'message'
EMAIL_SENT = u'email sent'
EMAIL_SENT_TO_USER = u'email sent to user(s)'

CLICK_ON_LINK_TO_VERIFY_EMAIL = u'click on the following link to verify your email'
CLICK_ON_LINK_TO_RESET_PASSWORD = u'click on the following link to reset your password'
CLICK_HERE = u'click here'

SELECT_ALL = u'select all'
UNSELECT_ALL = u'unselect all'

DID_YOU_MEAN = u'did you mean'

NEW_VERSION_AVAILABLE = u'&rarr; A new Chimithèque version is available: {version}, ask your administrator to install it from <a href="{download_url}">here</a>.'

ERROR_MSG = u'''
                      Oups !
                      <br/>
                      <br/>
                      An error occurred.<br/>
                      Please send an email to the chimitheque@cru.fr mailing list with the following informations:<br/><br/>
                      {error_code_txt} : {error_code}<br/>
                      {requested_uri_txt} : {requested_uri}<br/>
                      {request_url_txt} : {request_url}<br/><br/>
                      and download and join to your message the file below.
                      <br/>
                      <br/>
                      Thanks.
                      '''
ERROR_CODE = u'error code'
ERROR_REQUESTED_URI = u'error requested URI'
ERROR_REQUEST_URL = u'error request URL'
ERROR_TICKET = u'error ticket'
ERROR_FILE = u'download the error file'

INDEX_NB_PRODUCT_CARD = u'number of product cards'
INDEX_NB_product_STORED = u'number of products stored in your entity(ies)'
INDEX_SESSION_TIME_MESSAGE = u'you will be logged out after %s minutes of inactivity'
INDEX_LAST_ANNOUNCEMENT = u'last 10 messages'
INDEX_VIEW_ANNOUNCEMENT = u'view messages'
INDEX_LEGEND = u'legend'

MENU_QUICK_REQUEST = u'quick request'

MENU_TOOLS = u'tools'
MENU_SYSTEM_TOOLS = u'system tools'
MENU_ADD_PC = u'add a product card'
MENU_SEARCH_PC = u'search a product card'
MENU_ALL_PC = u'all product cards'
MENU_ORPHAN_PC = u'ophan product cards'
MENU_PC_ORG = u'product stored in the organization'
MENU_PC_BORROW_ENTITY = u'products borrowed in my entities'
MENU_MANAGE_USER = u'manage users/store locations/entities'
MENU_MANAGE_COC = u'manage classes of compounds'
MENU_MANAGE_PHYSICAL_STATE = u'manage physical states'
MENU_MANAGE_SUP = u'manage suppliers'
MENU_ARCHIVE = u'storage cards archives'
MENU_ADMIN = u'tools'
MENU_EXPOSURE_CARD = u'my exposure cards'
MENU_LIST_COM = u'current commands'
MENU_LIST_COM_ALL = u'all the commands'
MENU_LIST_COM_NEW = u'new commands'
MENU_LIST_COM_ACCEPTED = u'accepted commands'
MENU_LIST_COM_MINE = u'my commands'

PRODUCT = u'product'
STORAGE = u'storage'

DB_CPE_LABEL = u'CPE'
DB_CPE_COMMENT = u'collective protective equipment'

DB_PPE_LABEL = u'PPE'
DB_PPE_COMMENT = u'personal protective equipment'

CREATE_EXPOSURE_CARD = u'create a new exposure card'
EXPOSURE_CARD_CREATED = u'exposure card created'
EXPOSURE_CARD_UPDATED = u'exposure card updated'
EXPOSURE_CARD_DELETED = u'exposure card deleted'
VIEW_EXPOSURE_CARD = u'view this exposure card'
DELETE_EXPOSURE_CARD = u'delete this exposure card'
DELETE_EXPOSURE_ITEM = u'delete this line'
EXPOSURE_CARD_ADD_ITEM = u'search and add a new product'
EXPOSURE_CARD_ACTIVATE = u'activate this exposure card'

EXPOSURE_CARD_PRODUCT_ALREADY_PRESENT_ERROR = u'product already present'

COMMAND = u'command'
CREATE_COMMAND = u'create a command'
DELETE_COMMAND = u'delete command'
COMMAND_CREATED = u'command created'
COMMAND_UPDATED = u'command updated'
COMMAND_DELETED = u'command deleted'
COMMAND_ADD_FOR_PRODUCT = u'Add a command for the product:'
COMMAND_EDIT_FOR_PRODUCT = u'Edit the command for the product:'
COMMAND_LIST_PRODUCT = u'Product'
COMMAND_LIST_SUBMITTER = u'Submitter'
COMMAND_LIST_STATUS = u'Status'
COMMAND_LIST_VOLUME = u'Volume/Weight'
COMMAND_LIST_CREATION = u'Creation'
COMMAND_LIST_MODIFICATION = u'Modification'
COMMAND_LIST_SUPPLIER = u'Supplier'
COMMAND_LIST_RETAILER = u'Retailer'
COMMAND_LIST_UNIT_PRICE = u'Unit price'
COMMAND_LIST_FUNDS = u'Funds'
COMMAND_LIST_ENTITY = u'Entity'
COMMAND_LIST_SUBTEAM = u'Subteam'
COMMAND_LIST_REFERENCE = u'Reference'
COMMAND_LIST_PRODUCT_REFERENCE = u'Product reference'
COMMAND_LIST_STORE_LOCATION = u'Store location'
COMMAND_LIST_COMMENT = u'Comment'
COMMAND_LIST_ACTIONS = u'Actions'
COMMAND_LIST_MODIFIER = u'Modifier'
COMMAND_LIST_BEFORE_STATUS = u'Before status'
COMMAND_LIST_AFTER_STATUS = u'After status'
COMMAND_EDIT = u'Edit'
COMMAND_CLONE = u'Clone'
COMMAND_HISTORY = u'History'
COMMAND_UPDATE_MESSAGE_SUBJECT = u'update on your Chimitheque command'
COMMAND_UPDATE_MESSAGE_BODY = """
                    Hello %s,
                    The status of your command for %s of %s has been changed
                    From: %s
                    To: %s
                    Thanks for using Chimitheque.
                    The Chimitheque team.
                    """

DB_EXPOSURE_CARD_ACCIDENTAL_EXPOSURE_TYPE_LABEL = u'accidental exposure type'
DB_EXPOSURE_CARD_ACCIDENTAL_EXPOSURE_TYPE_COMMENT = u''
DB_EXPOSURE_CARD_ACCIDENTAL_EXPOSURE_DATETIME_LABEL = u'date and time'
DB_EXPOSURE_CARD_ACCIDENTAL_EXPOSURE_DATETIME_COMMENT = u''
DB_EXPOSURE_CARD_ACCIDENTAL_EXPOSURE_DURATION_AND_EXTENT_LABEL = u'duration and extent'
DB_EXPOSURE_CARD_ACCIDENTAL_EXPOSURE_DURATION_AND_EXTENT_COMMENT= u''
DB_EXPOSURE_ITEM_CREATION_DATETIME_LABEL = u'creation date'
DB_EXPOSURE_ITEM_CREATION_DATETIME_COMMENT = u''
DB_EXPOSURE_ITEM_PRODUCT_LABEL = u'product'
DB_EXPOSURE_ITEM_PRODUCT_COMMENT = u''
DB_EXPOSURE_ITEM_KIND_OF_WORK_LABEL = u'kind of work'
DB_EXPOSURE_ITEM_KIND_OF_WORK_COMMENT = u'ex: weighing, gel and hybridization'
DB_EXPOSURE_ITEM_CPE_LABEL = u'CPE'
DB_EXPOSURE_ITEM_CPE_COMMENT = u''
DB_EXPOSURE_ITEM_PPE_LABEL = u'PPE'
DB_EXPOSURE_ITEM_PPE_COMMENT = u''
DB_EXPOSURE_ITEM_NB_EXPOSURE_LABEL = u'number of exposure per year'
DB_EXPOSURE_ITEM_NB_EXPOSURE_COMMENT = u''
DB_EXPOSURE_ITEM_EXPOSURE_TIME_LABEL = u'exposure time for each manipulation'
DB_EXPOSURE_ITEM_EXPOSURE_TIME_COMMENT = u''
DB_EXPOSURE_ITEM_SIMULTANEAOUS_RISK_LABEL = u'simultaneous risk'
DB_EXPOSURE_ITEM_SIMULTANEAOUS_RISK_COMMENT = u''

DB_HAZARD_CODE_LABEL = u'label'
DB_HAZARD_CODE_COMMENT = u'ex: C (for corrosive)'
DB_SYMBOL_LABEL = u'label'
DB_SYMBOL_COMMENT = u'ex: SGH02'
DB_SIGNAL_WORD_LABEL = u'label'
DB_SIGNAL_WORD_COMMENT = u'attention | danger'
DB_PHYSICAL_STATE_LABEL = u'label'
DB_PHYSICAL_STATE_COMMENT = u''
DB_CLASS_OF_COMPOUNDS_LABEL = u'label'
DB_CLASS_OF_COMPOUNDS_COMMENT = u''
DB_SUPPLIER_LABEL = u'label'
DB_SUPPLIER_COMMENT = u''
DB_RISK_PHRASE_LABEL = u'label'
DB_RISK_PHRASE_COMMENT = u'ex: Explosive when dry'
DB_RISK_PHRASE_REFERENCE_LABEL = u'reference'
DB_RISK_PHRASE_REFERENCE_COMMENT = u'ex: R1'
DB_SAFETY_PHRASE_LABEL = u'label'
DB_SAFETY_PHRASE_COMMENT = u'ex: Keep locked up'
DB_SAFETY_PHRASE_REFERENCE_LABEL = u'reference'
DB_SAFETY_PHRASE_REFERENCE_COMMENT = u'ex: S1'
DB_HAZARD_STATEMENT_LABEL = u'label'
DB_HAZARD_STATEMENT_COMMENT = u''
DB_HAZARD_STATEMENT_REFERENCE_LABEL = u'reference'
DB_HAZARD_STATEMENT_REFERENCE_COMMENT = u''
DB_PRECAUTIONARY_STATEMENT_LABEL = u'label'
DB_PRECAUTIONARY_STATEMENT_COMMENT = u''
DB_PRECAUTIONARY_STATEMENT_REFERENCE_LABEL = u'reference'
DB_PRECAUTIONARY_STATEMENT_REFERENCE_COMMENT = u''
DB_EMPIRICAL_FORMULA_LABEL = u'label'
DB_EMPIRICAL_FORMULA_COMMENT = u''
DB_LINEAR_FORMULA_LABEL = u'label'
DB_LINEAR_FORMULA_COMMENT = u''
DB_NAME_LABEL = u'label'
DB_NAME_COMMENT = u'ex: sodium hydroxide'
DB_ENTITY_ROLE_LABEL = u'name'
DB_ENTITY_ROLE_COMMENT = u''
DB_ENTITY_DESCRIPTION_LABEL = u''
DB_ENTITY_DESCRIPTION_COMMENT = u''
DB_ENTITY_MANAGER_LABEL = u'manager(s)'
DB_ENTITY_MANAGER_COMMENT = u''
DB_PERSON_FIRST_NAME_LABEL = u'first name'
DB_PERSON_FIRST_NAME_COMMENT = u'ex: John'
DB_PERSON_LAST_NAME_LABEL = u'last name'
DB_PERSON_LAST_NAME_COMMENT = u'ex: Doe'
DB_PERSON_EMAIL_LABEL = u'email'
DB_PERSON_EMAIL_COMMENT = u'this MUST be a valid email'
DB_PERSON_CONTACT_LABEL = u'contact'
DB_PERSON_CONTACT_COMMENT = u'any information to contact the person'
DB_PERSON_PASSWORD_LABEL = u'password'
DB_PERSON_PASSWORD_COMMENT = u'enter an enough secure password'
DB_PERSON_CREATION_DATE_LABEL = u'creation date'
DB_PERSON_CREATION_DATE_COMMENT = u''
DB_PERSON_REGISTRATION_KEY_LABEL = u'account status'
DB_PERSON_CREATOR_LABEL = u'creator'
DB_PERSON_CREATOR_COMMENT = u''
DB_MESSAGE_TEXT_LABEL = u'message'
DB_MESSAGE_TEXT_COMMENT = u''
DB_MESSAGE_TOPIC_LABEL = u'topic'
DB_MESSAGE_TOPIC_COMMENT = u''
DB_MESSAGE_TOPIC_DEFAULT = u'no topic'
DB_MESSAGE_CREATION_DATETIME_LABEL = u'creation date'
DB_MESSAGE_CREATION_DATETIME_COMMENT = u''
DB_MESSAGE_EXPIRATION_DATETIME_LABEL = u'expiration date'
DB_MESSAGE_EXPIRATION_DATETIME_COMMENT = u''
DB_MESSAGE_PERSON_LABEL = CREATED_UPDATED_BY
DB_MESSAGE_PERSON_COMMENT = u''
DB_MESSAGE_PIN_LABEL = u'pin'
DB_MESSAGE_PIN_COMMENT = u'only admins can pin messages'
DB_SHOUT_TEXT_LABEL = u'message'
DB_SHOUT_TEXT_COMMENT = u''
DB_SHOUT_CREATION_DATETIME_LABEL = u'on'
DB_SHOUT_CREATION_DATETIME_COMMENT = u''
DB_SHOUT_SENDER_LABEL = u'sender'
DB_SHOUT_SENDER_COMMENT = u'message from'
DB_SHOUT_RECEIVER_LABEL = u'to'
DB_SHOUT_RECEIVER_COMMENT = u'message to'
DB_STORE_LOCATION_LABEL = u'name'
DB_STORE_LOCATION_COMMENT = u''
DB_STORE_LOCATION_ENTITY_LABEL = u'entity'
DB_STORE_LOCATION_ENTITY_COMMENT = u''
DB_STORE_LOCATION_PARENT_LABEL = u'parent'
DB_STORE_LOCATION_PARENT_COMMENT = u''
DB_STORE_LOCATION_CAN_STORE_LABEL = u'can store'
DB_STORE_LOCATION_CAN_STORE_COMMENT = u'allow users to store products in this store location'
DB_STORE_LOCATION_COLOR_LABEL = u'color'
DB_STORE_LOCATION_COLOR_COMMENT = u'color of the labels in the storage lists'
DB_UNIT_LABEL = u'label'
DB_UNIT_COMMENT = u'ex: "g" for gram'
DB_UNIT_REFERENCE_LABEL = u'reference for this unit'
DB_UNIT_REFERENCE_COMMENT = u'ex: the reference for the unit "mg" is "g"'
DB_UNIT_MULTIPLIER_FOR_REFERENCE_LABEL = u'multiplier to obtain the reference unit'
DB_UNIT_MULTIPLIER_FOR_REFERENCE_COMMENT = u'ex: for "mg" the reference unit is "g" then the multiplier is "0.001"'

DB_PRODUCT_CAS_NUMBER_LABEL = u'CAS number'
DB_PRODUCT_CAS_NUMBER_COMMENT = u'must be a valid CAS number and the pair CAS/specificity MUST be unique - you can enter a CAS number that already exists but with another specificity'
DB_PRODUCT_CE_NUMBER_LABEL = u'CE number'
DB_PRODUCT_CE_NUMBER_COMMENT = u''
DB_PRODUCT_PERSON_LABEL = CREATED_UPDATED_BY
DB_PRODUCT_PERSON_COMMENT = u''
DB_PRODUCT_NAME_LABEL = u'product name'
DB_PRODUCT_NAME_COMMENT = u'you may use the syntax "stereochemistry@product_name" - look at the documentation - you can enter only one product name but several synonyms'
DB_PRODUCT_SYNONYM_LABEL = u'product synonym(s)'
DB_PRODUCT_SYNONYM_COMMENT = u'you may use the syntax "stereochemistry@product_synonym" - look at the documentation - you can enter only one product name but several synonyms'
DB_PRODUCT_RESTRICTED_ACCESS_LABEL = u'product with a restricted access'
DB_PRODUCT_RESTRICTED_ACCESS_COMMENT = u'visible only by people that have the "view restricted product cards" permission'
DB_PRODUCT_SPECIFICITY_LABEL = u'specificity'
DB_PRODUCT_SPECIFICITY_COMMENT = u'ex: anhydrous'
DB_PRODUCT_TD_FORMULA_LABEL = u'3D formula'
DB_PRODUCT_TD_FORMULA_COMMENT = u'a Web link to the 3 dimensions formula'
DB_PRODUCT_EMPIRICAL_FORMULA_LABEL = u'empirical formula'
DB_PRODUCT_EMPIRICAL_FORMULA_COMMENT = u'ex: C4H6O6' \
    + ' [note 1] the atoms will be automatically sorted: C, H and the other atoms in the alphabetical order'\
    + ' [note 2] salts and hydrous compounds must be typed like AgClO4.xH2O (put a dot and not a comma as a separator)'\
    + ' [note 3] use a comma (and not a dot) for decimal numbers'\
    + ' [note 4] numbers for isotopes must be precede by the sign ^'
DB_PRODUCT_LINEAR_FORMULA_LABEL = u'linear formula'
DB_PRODUCT_LINEAR_FORMULA_COMMENT = u'ex: HOOC(CHOH)2COOH'
DB_PRODUCT_MSDS_LABEL = u'MSDS link'
DB_PRODUCT_MSDS_COMMENT = u'enter the link to the MSDS card (from your supplier Web site for example)'
NO_MSDS = u'no MSDS'
DB_PRODUCT_PHYSICAL_STATE_LABEL = u'physical state'
DB_PRODUCT_PHYSICAL_STATE_COMMENT = u''
DB_PRODUCT_CLASS_OF_COMPOUNDS_LABEL = u'class(es) of compounds'
DB_PRODUCT_CLASS_OF_COMPOUNDS_COMMENT = u'you can select more than one class of compounds'
DB_PRODUCT_HAZARD_CODE_LABEL = u'hazard code(s)'
DB_PRODUCT_HAZARD_CODE_COMMENT = u''
DB_PRODUCT_SYMBOL_LABEL = u'symbol(s)'
DB_PRODUCT_SYMBOL_COMMENT = u''
DB_PRODUCT_SIGNAL_WORD_LABEL = u'signal word'
DB_PRODUCT_SIGNAL_WORD_COMMENT = u''
DB_PRODUCT_RISK_PHRASE_LABEL = u'risk phrase(es)'
DB_PRODUCT_RISK_PHRASE_COMMENT = u'enter the phrase number such as 20'
DB_PRODUCT_SAFETY_PHRASE_LABEL = u'safety phrase(es)'
DB_PRODUCT_SAFETY_PHRASE_COMMENT = u'enter the phrase number such as 20'
DB_PRODUCT_HAZARD_STATEMENT_LABEL = u'hazard statement(s) H-EUH'
DB_PRODUCT_HAZARD_STATEMENT_COMMENT = u'enter the statement number such as H200 or EUH001'
DB_PRODUCT_PRECAUTIONARY_STATEMENT_LABEL = u'precautionary statement(s) P'
DB_PRODUCT_PRECAUTIONARY_STATEMENT_COMMENT = u'enter the statement number such as P101'
DB_PRODUCT_DISPOSAL_COMMENT_LABEL = u'disposal comment'
DB_PRODUCT_DISPOSAL_COMMENT_COMMENT = u''
DB_PRODUCT_REMARK_LABEL = u'remark'
DB_PRODUCT_REMARK_COMMENT = u''
DB_PRODUCT_IS_CMR_LABEL = u'CMR'
DB_PRODUCT_IS_CMR_COMMENT = u'is this product a CMR?'
DB_PRODUCT_IS_RADIO_LABEL = u'Radioactive'
DB_PRODUCT_IS_RADIO_COMMENT = u'is this product radioactive?'
DB_PRODUCT_CMR_CATEGORY_LABEL = u'CMR category'
DB_PRODUCT_CREATION_DATETIME_LABEL = u'creation date'
DB_PRODUCT_CREATION_DATETIME_COMMENT = u''

DB_STORAGE_PRODUCT_LABEL = u'product'
DB_STORAGE_PRODUCT_COMMENT = u''
DB_STORAGE_PERSON_LABEL = CREATED_UPDATED_BY
DB_STORAGE_PERSON_COMMENT = u''
DB_STORAGE_STORE_LOCATION_LABEL = u'store location'
DB_STORAGE_STORE_LOCATION_COMMENT = u''
DB_STORAGE_VOLUME_WEIGHT_LABEL = u'volume or weight'
DB_STORAGE_VOLUME_WEIGHT_COMMENT = u'leave it empty if you do not want to enter a volume or weight'
DB_STORAGE_UNIT_LABEL = u'unit'
DB_STORAGE_UNIT_COMMENT = u''
DB_STORAGE_NB_ITEMS_LABEL = u'nb items'
DB_STORAGE_NB_ITEMS_COMMENT = u'number of items (bottles, boxes...)'
DB_STORAGE_CREATION_DATETIME_LABEL = u'creation date'
DB_STORAGE_CREATION_DATETIME_COMMENT = u''
DB_STORAGE_ENTRY_DATETIME_LABEL = u'entry date'
DB_STORAGE_ENTRY_DATETIME_COMMENT = u''
DB_STORAGE_EXIT_DATETIME_LABEL = u'exit date'
DB_STORAGE_EXIT_DATETIME_COMMENT = u''
DB_STORAGE_EXPIRATION_DATETIME_LABEL = u'expiration date'
DB_STORAGE_EXPIRATION_DATETIME_COMMENT = u''
DB_STORAGE_OPENING_DATETIME_LABEL = u'opening date'
DB_STORAGE_OPENING_DATETIME_COMMENT = u''
DB_STORAGE_COMMENT_LABEL = u'comment'
DB_STORAGE_COMMENT_COMMENT = u''
DB_STORAGE_BARECODE_LABEL = u'barecode'
DB_STORAGE_BARECODE_COMMENT = u'auto-generated by the application'
DB_STORAGE_REFERENCE_LABEL = u'reference'
DB_STORAGE_REFERENCE_COMMENT = u'supplier reference'
DB_STORAGE_BATCH_NUMBER_LABEL = u'batch number'
DB_STORAGE_BATCH_NUMBER_COMMENT = u'supplier batch number'
DB_STORAGE_SUPPLIER_LABEL = u'supplier'
DB_STORAGE_SUPPLIER_COMMENT = u''
DB_STORAGE_ARCHIVE_LABEL = u'archive'
DB_STORAGE_ARCHIVE_COMMENT = u''
DB_STORAGE_TO_DESTROY_LABEL = u'to destroy'
DB_STORAGE_TO_DESTROY_COMMENT = u''

DB_STOCK_MAXIMUM_LABEL = u'maximum volume or weight in entity'
DB_STOCK_MAXIMUM_COMMENT = u''
DB_STOCK_MINIMUM_LABEL = u'minimum volume or weight in entity'
DB_STOCK_MINIMUM_COMMENT = u''
DB_STOCK_MAXIMUM_UNIT_LABEL = u'unit'
DB_STOCK_MAXIMUM_UNIT_COMMENT = u''
DB_STOCK_MINIMUM_UNIT_LABEL = u'unit'
DB_STOCK_MINIMUM_UNIT_COMMENT = u''
DB_STOCK_CURRENT_LABEL = u'current volume or weight in entity'
DB_STOCK_CURRENT_COMMENT = u''
DB_STOCK_PRODUCT_LABEL = u'product'
DB_STOCK_PRODUCT_COMMENT = u''
DB_STOCK_ENTITY_LABEL = u'entity'
DB_STOCK_ENTITY_COMMENT = u''

DB_STOCK_STORE_LOCATION_CURRENT_LABEL = u'current volume or weight in store location'
DB_STOCK_STORE_LOCATION_CURRENT_COMMENT = u''
DB_STOCK_STORE_LOCATION_PRODUCT_LABEL = u'product'
DB_STOCK_STORE_LOCATION_PRODUCT_COMMENT = u''
DB_STOCK_STORE_LOCATION_SL_LABEL = u'store location'
DB_STOCK_STORE_LOCATION_SL_COMMENT = u''

DB_USE_CREATION_DATETIME_LABEL = u'borrow date'
DB_USE_CREATION_DATETIME_COMMENT = u''
DB_USE_PERSON_LABEL = CREATED_UPDATED_BY
DB_USE_PERSON_COMMENT = u''
DB_USE_BORROWER_LABEL = u'borrowed by'
DB_USE_BORROWER_COMMENT = u''
DB_USE_STORAGE_LABEL = u'borrowed storage'
DB_USE_STORAGE_COMMENT = u''
DB_USE_COMMENT_LABEL = u'comment'
DB_USE_COMMENT_COMMENT = u''

DB_COMMAND_SUBMITTER_LABEL = u'submitter'
DB_COMMAND_SUBMITTER_COMMENT = u''
DB_COMMAND_STATUS_LABEL = u'status'
DB_COMMAND_STATUS_COMMENT = u''
DB_COMMAND_VOLUME_WEIGHT_LABEL = DB_STORAGE_VOLUME_WEIGHT_LABEL
DB_COMMAND_VOLUME_WEIGHT_COMMENT = DB_STORAGE_VOLUME_WEIGHT_COMMENT
DB_COMMAND_UNIT_LABEL = DB_STORAGE_UNIT_LABEL
DB_COMMAND_UNIT_COMMENT = DB_STORAGE_UNIT_COMMENT
DB_COMMAND_NB_ITEMS_LABEL = DB_STORAGE_NB_ITEMS_LABEL
DB_COMMAND_NB_ITEMS_COMMENT = DB_STORAGE_NB_ITEMS_COMMENT
DB_COMMAND_SUPPLIER_LABEL = u'supplier'
DB_COMMAND_SUPPLIER_COMMENT = u''
DB_COMMAND_UNIT_PRICE_LABEL = u'unit price'
DB_COMMAND_UNIT_PRICE_COMMENT = u''
DB_COMMAND_FUNDS_LABEL = u'funds'
DB_COMMAND_FUNDS_COMMENT = u''
DB_COMMAND_REFERENCE_LABEL = u'command reference'
DB_COMMAND_REFERENCE_COMMENT = u''
DB_COMMAND_PRODUCT_REFERENCE_LABEL = u'product reference'
DB_COMMAND_PRODUCT_REFERENCE_COMMENT = u''
DB_COMMAND_RETAILER_LABEL = u'retailer'
DB_COMMAND_RETAILER_COMMENT = u''
DB_COMMAND_STORE_LOCATION_LABEL = u'store location'
DB_COMMAND_STORE_LOCATION_COMMENT = u''
DB_COMMAND_ENTITY_LABEL = u'entity'
DB_COMMAND_ENTITY_COMMENT = u''
DB_COMMAND_SUBTEAM_LABEL = u'subteam'
DB_COMMAND_SUBTEAM_COMMENT = u''
DB_COMMAND_COMMENT_LABEL = u'comment'
DB_COMMAND_COMMENT_COMMENT = u''
DB_COMMAND_LOG_MODIFIER_LABEL = u'modified by'
DB_COMMAND_LOG_MODIFIER_COMMENT = u''
DB_COMMAND_LOG_BEFORE_STATUS_LABEL = u'before status'
DB_COMMAND_LOG_BEFORE_STATUS_COMMENT = u''
DB_COMMAND_LOG_AFTER_STATUS_LABEL = u'after status'
DB_COMMAND_LOG_AFTER_STATUS_COMMENT = u''
DB_COMMAND_LOG_DATETIME_LABEL = u'modification date'
DB_COMMAND_LOG_DATETIME_COMMENT = u''

WELCOME_TO = u'welcome to'
WELCOME = u'welcome'

SITE_OPTIMIZED_TO_RUN = u'site optimized to run under Mozilla Firefox and Google Chrome'
PROJECT_WEB_SITE = u'project Web site'

FIX_FORMULA = u'fix formula(s)'
FORMULA_CAN_BE_FIXED = u'formula(s) that can be fixed'
FORMULA_CAN_NOT_BE_FIXED = u'formula(s) that can not be fixed'

ADMIN_TOOL_SEND_EMAIL = u'send an email to every user'
ADMIN_TOOL_LIST_ORPHAN_PRODUCT_name = u'list orphan product names'
ADMIN_TOOL_LIST_ORPHAN_EMPIRICAL_FORMULA = u'list orphan empirical formulas'
ADMIN_TOOL_LIST_WRONG_EMPIRICAL_FORMULA = u'list wrong empirical formulas'
ADMIN_TOOL_DATABASE = u'manage database'
ADMIN_TOOL_EXPORT_PRODUCT_DATABASE = u'export product database'
ADMIN_TOOL_IMPORT_PRODUCT_DATABASE = u'import product database'
ADMIN_TOOL_CLEAN_DATABASE = u'clean database'
ADMIN_TOOL_PRODUCT_CARD_PER_USER = u'product cards per user'
ADMIN_TOOL_STORAGE_CARD_PER_USER = u'storage cards per user'
ADMIN_TOOL_UPDATE_NAME_COMPUTED_FIELD = u'update product names computed field'
ADMIN_TOOL_COMPUTE_STOCK = u'compute stock'
ADMIN_TOOL_STATISTIC = u'statistics'
ADMIN_TOOL_MANAGE_TABLE_ENTRIES = u'manage tables entries'

DATABASE_CLEANED = u'database cleaned'
CLEAN_DATABASE = u'clean database'

ORPHAN_EMPIRICAL_FORMULA = u'orphan empirical formula(s)'
ORPHAN_LINEAR_FORMULA = u'orphan linear formula(s)'
ORPHAN_NAME = u'orphan name(s)'
WRONG_FORMULA = u'wrong formula(s)'
WRONG_FORMULA_CAN_BE_FIXED = u'wrong formula(s) that can be fixed'
WRONG_FORMULA_CAN_NOT_BE_FIXED = u'wrong formula(s) that can not be fixed'

PERMISSION_SELECT = u'list'
PERMISSION_READ = u'view (details)'
PERMISSION_CREATE = u'create'
PERMISSION_UPDATE = u'update'
PERMISSION_DELETE = u'delete'
PERMISSION_IN_HIS_ENTITY = u'in his entity(ies) only'
PERMISSION_HIS_MESSAGE = u'his messages only'
PERMISSION_QUICK_SELECT = u'quick select permissions'
PERMISSION_QUICK_SELECT_1 = u'1: read/update/create product cards'
PERMISSION_QUICK_SELECT_2 = u'2: read/update storage cards (can not create new storage cards)'
PERMISSION_QUICK_SELECT_3 = u'3: 1 + 2 + write storage cards'
PERMISSION_QUICK_SELECT_4 = u'4: 3 + read/delete storage card archives'
PERMISSION_QUICK_SELECT_5 = u'5: 1 + full rights for user and store location'
PERMISSION_QUICK_SELECT_6 = u'6: full rights except for entities'

ADMINISTRATOR = u'administrator(s)'
VIRTUAL = u'virtual(s)'
USER_ALL_ENTITY = u'user(s) in all entities'

PERSON_CREATED = u'person created'
PERSON_UPDATED = u'person updated'
PERSON_DELETED = u'person deleted'
PERSON_CAN_NOT_BE_DELETED = u'this person can not be deleted'
CREATE_PERSON = u'create user'
UPDATE_PERSON = u'update user'
DELETE_PERSON = u'delete user'
IMPERSONATE_PERSON = u'impersonate user'
UNIMPERSONATE_PERSON = u'unimpersonate user'
PERSON_SEARCH_LDAP = u'search a user (part of name) in the directory'
PERSON_CREATE_ADVICE = u'an email is sent to the user after the creation to initialize the password'
PERSON_PENDING = u'pending'
PERSON_STATUS = u'status'
PERSON_UNACTIVE = u'unactive'
PERSON_DISABLED = u'disabled'
PERSON_NOT_VERIFIED = u'email not verified'
PERSON_ACTIVE = u'active'
PERSON_NO_ENTITY = u'without entity'
NO_PERSON = u'no user'
PERSON_DELETE_ADVICE = u'only people with no (archived) storages can be deleted'

PERSON = u'person'
PERSON_ENTITY_LABEL = u'entity(ies)'
PERSON_ENTITY_COMMENT = u'several entities allowed'
PERSON_IS_ADMIN_LABEL = u'is admin'
PERSON_IS_ADMIN_COMMENT = u'will have full rights and belongs to every entity (current and future)'
PERSON_IS_VIRTUAL_LABEL = u'is virtual'
PERSON_IS_VIRTUAL_COMMENT = u'enter a fake email such as students@univ.fr - you will receive the password by mail for this account'
PERSON_IS_ALL_ENTITY_LABEL = u'is in all entities'
PERSON_IS_ALL_ENTITY_COMMENT = u'will belongs to every entity (current and future)'
PERSON_ENTITY_PERMISSION_LABEL = u'permissions'
PERSON_ENTITY_PERMISSION_COMMENT = u'checkboxes with a dot can not be modified'
PERSON_RESET_PASSWORD = u'your password has been changed'
PERSON_CREATION_MESSAGE_SUBJECT = u'your Chimitheque account'
PERSON_VIRTUAL_CREATION_MESSAGE_SUBJECT = u'your virtual Chimitheque account'
PERSON_CREATION_MESSAGE_BODY = """
                    Hello %s,
                    Your account on Chimitheque has been created.
                    Your login is: %s
                    Please setup your password on the following URL: %s/default/user/reset_password?key=%s
                    Thanks for using Chimitheque.
                    The Chimitheque team.
                    """
PERSON_VIRTUAL_CREATION_MESSAGE_BODY = """
                    Hello %s,
                    Your virtual account on Chimitheque has been created.
                    Your virtual login is: %s
                    Your virtual password is: %s
                    Thanks for using Chimitheque.
                    The Chimitheque team.
                    """
PERSON_CREATOR_LABEL = u'creator'
ENABLE_PERSON = u'enable person'
DISABLE_PERSON = u'disable person'
PRODUCT_CREATED = u'product created'
PRODUCT_UPDATED = u'product updated'
PRODUCT_DELETED = u'product deleted'
PRODUCT_CAN_NOT_BE_DELETED = u'this product can not be deleted'
PRODUCT_NOT_ORPHAN = u'this product is not orphan (then can not be deleted)'
PRODUCT_WITH_SAME_CAS = u'product(s) with the same CAS number'
CAS_AVAILABLE = u'CAS number available'
CAS_ERROR = u'CAS error'

ENTITY = u'entity'
ENTITY_CREATED = u'entity created'
ENTITY_UPDATED = u'entity updated'
ENTITY_DELETED = u'entity deleted'
CREATE_ENTITY = u'create entity'
UPDATE_ENTITY = u'update entity'
DELETE_ENTITY = u'delete entity'
NO_ENTITY = u'no entity'
ENTITY_CAN_NOT_BE_DELETED = u'this entity can not be deleted'
ENTITY_USER = u'user(s)'
ENTITY_STORE_LOCATION = u'store location(s)'
ENTITY_DELETE_ADVICE = u'only entities with no people and no store locations can be deleted'

SWITCH_VIEW_BY_ENTITY = u'switch to the view by entity'
SWITCH_VIEW_BY_USER = u'switch to the view by user'

PHYSICAL_STATE = u'physical states'
PHYSICAL_STATE_CREATED = u'physical state created'
PHYSICAL_STATE_UPDATED = u'physical state updated'
PHYSICAL_STATE_DELETED = u'physical state deleted'
PHYSICAL_STATE_DELETE_ADVICE = u'deleting a physical state does not delete linked product cards'
CREATE_PHYSICAL_STATE = u'create physical state'
UPDATE_PHYSICAL_STATE = u'update physical state'
DELETE_PHYSICAL_STATE = u'delete physical state'
NO_PHYSICAL_STATE = u'no physical state'

COC = u'class of compounds'
COC_CREATED = u'class of compounds created'
COC_UPDATED = u'class of compounds updated'
COC_DELETED = u'class of compounds deleted'
COC_DELETE_ADVICE = u'deleting a class of compounds does not delete linked product cards'
CREATE_COC = u'create class of compounds'
UPDATE_COC = u'update class of compounds'
DELETE_COC = u'delete class of compounds'
NO_COC = u'no class of compounds'

MESSAGE = u'message(s)'
CREATE_MESSAGE = u'create message'
UPDATE_MESSAGE = u'update message'
DELETE_MESSAGE = u'delete message'
ANSWER_MESSAGE = u'answer message'
FORGET_MESSAGE = u'forget message'
NO_TOPIC = u'no topic'

SHOUT_CREATED = u'message sent'

LINKED_PRODUCT_CARD = u'linked product card(s)'
LINKED_STORAGE_CARD = u'linked storage card(s)'
LINKED_ARCHIVED_STORAGE_CARD = u'linked archived storage card(s)'
LINKED_ENTITY = u'linked entity(ies)'

STORE_LOCATION = u'store location'
STORE_LOCATION_CREATED = u'store location created'
STORE_LOCATION_UPDATED = u'store location updated'
STORE_LOCATION_DELETED = u'store location deleted'
STORE_LOCATION_CAN_NOT_BE_DELETED = u'store location can not be deleted'
STORE_LOCATION_LIST_ADVICE = u'to store a product in a store location, search it then click on it and click on the "store this product in my entity" icon'
NO_STORE_LOCATION = u'no store location'
CREATE_STORE_LOCATION = u'create store location'

SUPPLIER = u'supplier'
SUPPLIER_CREATED = u'supplier created'
SUPPLIER_UPDATED = u'supplier updated'
SUPPLIER_DELETED = u'supplier deleted'
CREATE_SUPPLIER = u'create supplier'
UPDATE_SUPPLIER = u'update supplier'
DELETE_SUPPLIER = u'delete supplier'
SUPPLIER_DELETE_ADVICE = u'deleting a supplier does not delete linked storage cards'
NO_SUPPLIER = u'no supplier'

STORAGE_CREATED = u'storage created'
STORAGE_UPDATED = u'storage updated'
STORAGE_DELETED = u'storage deleted'
UPDATE_STORE_LOCATION = u'update store location'
DELETE_STORE_LOCATION = u'delete store location'
STORE_LOCATION_DELETE_ADVICE = u'only store locations with no (archived) storages can be deleted'

SC = u'SC'
ARCHIVED_SC = u'archived SC'
ARCHIVE_DELETE_ADVICE = u'You have searched archived storage cards. For a better management, select the storage view'
STORAGE_CARD = u'storage card'
STORAGE_HISTORY = u'storage card history'
STORAGE_HISTORY_LIST = u'storage card history list'
STORAGE_ARCHIVE = u'storage card archive'
STORAGE_ARCHIVE_LIST = u'storage card archive list'
UPDATE_STORAGE_CARD = u'update storage card'
CLONE_STORAGE_CARD = u'clone storage card'
DELETE_STORAGE_CARD = u'delete selected storage card(s)'
DESTROY_STORAGE_CARD = u'mark with storage for destruction (does not delete the storage card)'
UNDESTROY_STORAGE_CARD = u'unmark with storage for destruction'
DELETE_ARCHIVED_STORAGE_CARD = u'delete archived storage card'
NO_VOLUME_WEIGHT = u'no volume or weight'

ARCHIVE = u'archive(s)'

BORROWER = u'borrower'
BORROW_STORAGE = u'borrow/give back storage'
BORROWING_CREATED = u'borrowing created'
BORROWING_UPDATED = u'borrowing updated'
BORROWING_DELETED = u'borrowing deleted'
UPDATE_BORROWING = u'update borrowing'
CHECK_TO_GIVE_BACK = u'check to give back'

STORE_INFO = u'when your store a product, a barecode is automatically generated and displayed after the form submission'

LEGEND = u'legend'
PRODUCT_IS_CMR = u'this product is a CMR'
PRODUCT_IS_RADIO = u'this product is radioactive'

EXPORT_IN_CSV = u'export in CSV - field separator=tabulation and text separator=double quote'
EXPORT_IN_CSV_TIP = u'if you want to export the stocks select the "display by storage" view'
EXPORT_IN_HTLM = u'export in HTML'

MODIFIED = u'modified'
MODIFIED_AT = u'modified at'

ENTER_A_LABEL = u'enter a label'

COC_ALREADY_EXIST = u'this class of compounds already exists'
SUPPLIER_ALREADY_EXIST = u'this supplier already exists'

REQUIRED_FIELDS = u'required fields'
MISSING_FIELDS = u'required fields are missing'

NCE = u'no CAS number (NCE, mixture,...)'

PRODUCT_IN_MY_ENTITY = u'products stored in my entity'
PRODUCT_IN_OTHER_ENTITY = u'products stored in other entity(ies)'
PRODUCT_IN_ENTITY = u'products stored in entity'
PRODUCT_STORED_AT = u'products stored at'
PRODUCT_IN_STORE_LOCATION = u'products stored in store location'
ALL_PRODUCT = u'all product cards'
ORPHAN_PRODUCT = u'orphan product cards'
NO_PRODUCT_MATCH = u'sorry, no result match your request'

STOCK = u'stock'

FIRST = u'first'
LAST = u'last'
PAGE = u'page(s)'
RESULT_PER_PAGE = u'results per page'
RESULT = u'result(s)'

CLOSE_WINDOW = u'close window'
CLOSE_LIST = u'close list'

PC = u'PC'
PRODUCT_CARD = u'product card'
PRODUCT_CARD_RESTRICTED = u'restricted product card'
PRODUCT_CARD_BROKEN_REFERENCE=u'product card with broken references'
UPDATE_PRODUCT_CARD = u'update product card'
CLONE_PRODUCT_CARD = u'clone product card'
DELETE_PRODUCT_CARD = u'delete product card'
PRODUCT_HISTORY = u'product card history'
PRODUCT_HISTORY_LIST = u'product card history list'

CONFIRM = u'are you sure that you want to do this action?'

EDIT = u'edit'

JUMP_TO_SECTION = u'jump to section'

BOOKMARK = u'add bookmark'
UNBOOKMARK = u'remove bookmark'
QUICK_DELETE_EXPOSURE_CARD = u'remove this product from my active exposure card'
QUICK_ADD_EXPOSURE_CARD = u'add this product to my active exposure card'

SECTION_RESTRICTED_ACCESS = u'restricted access'
SECTION_CAS_AND_CE = u'CAS and CE numbers'
SECTION_NAME = u'name and synonym(s)'
SECTION_DETAIL = u'details'
SECTION_FORMULA = u'chemical formula(s)'
SECTION_MSDS = u'MSDS link'
SECTION_SYMBOL = u'symbol(s)'
SECTION_PHRASE = u'phrase(s)'
SECTION_REMARK = u'remarks'

NO_EMPIRICAL_FORMULA = u'no empirical formula'
ADD_COC_TO_LIST = u'add a new class of compounds to the list'
ADD_SUPPLIER_TO_LIST = u'add a new supplier to the list'

MAGICAL_SELECTOR = u'magical selector'
COPY_AND_PASTE_FOR_MAGIC = u'copy/paste text here, and click on the button to create the magical effect'
DO_THE_MAGIC = u'do the magic'

EMPIRICAL_FORMULA_TESTER = u'empirical formula tester'
DISPLAY_NORMALIZED_EMPIRICAL_FORMULA = u'display the normalized empirical formula or an error'
CALCULATE_EMPIRICAL_FORMULA = u'linear formula -> empirical formula'

EMPIRICAL_FORMULA_ERROR_MAIN_SYNTAX = u'general syntax error'
EMPIRICAL_FORMULA_ERROR_WRONG_BRACKET = u'wrong bracket error'
EMPIRICAL_FORMULA_ERROR_DUPLICATED_ULATOMS = u'duplicated UPERCASElowercase atoms'
EMPIRICAL_FORMULA_ERROR_DUPLICATED_CATOMS = u'duplicated C atoms'
EMPIRICAL_FORMULA_ERROR_DUPLICATED_HATOMS = u'duplicated H atoms'
EMPIRICAL_FORMULA_ERROR_DUPLICATED_OTHERATOMS = u'duplicated UPERCASE atoms'
EMPIRICAL_FORMULA_ERROR_MORE_THAT_ONE_DOT = u'not permitted character'
EMPIRICAL_FORMULA_ERROR_LOWERCASE_ATOMS = u'atoms in lowercase or number error'
EMPIRICAL_FORMULA_ERROR_WRONG_ATOMS = u'wrong atoms'

CAS_NUMBER_CHECK_DIGIT_ERROR = u'CAS number error - check digit not verified'
CAS_NUMBER_WRONG_FORMAT_ERROR = u'CAS number error - wrong format'

STORE_PRODUCT_IN_MY_ENTITY = u'store this product in my entity'

STORAGE_DETAIL = u'product storage details'
IN_OTHER_ENTITY = u'in other entity(ies)'

EDIT_STOCK = u'edit stock'
MINIMUM_STOCK = u'minimum stock'
MAXIMUM_STOCK = u'maximum stock'
CURRENT_STOCK = u'current stock'
TOTAL = u'total'
TOTAL_FOR_REQUEST = u'total volume or weight for the request in the selected store location(s) or entity(ies)'

SEARCH = u'search'
ADVANCED_SEARCH = u'advanced search'
SEARCH_IS_IN_ENTITY = u'is in entity'
SEARCH_IS_IN_STORE_LOCATION = u'is in store location'
SEARCH_INCLUDE_CHILDREN_STORE_LOCATION = u'include children'
SEARCH_IS_A_CMR = u'is a CMR'
SEARCH_IS_RADIO = u'is radioactive'
SEARCH_ARCHIVE = u'products that have archived storage cards'
SEARCH_TO_DESTROY = u'is marked for destruction'
SEARCH_CAS_NUMBER = u'CAS number is'
SEARCH_CE_NUMBER = u'CE number is'
SEARCH_PRODUCT_CREATION_AFTER = u'product card creation date after'
SEARCH_STORAGE_ENTRY_AFTER = u'(storage card) entry date after'
SEARCH_STORAGE_EXIT_BEFORE = u'(storage card) exit date before'
SEARCH_STORAGE_BARECODE = u'barecode like'
SEARCH_NAME = u'name or synonym(s) like'
SEARCH_EMPIRICAL_FORMULA = u'empirical formula is'
SEARCH_LINEAR_FORMULA = u'linear formula is'
SEARCH_EXACT_COC = u'exact class(es) of compounds?'
SEARCH_COC = u'class(es) of compounds'
SEARCH_RISK_PHRASE = u'start typing the phrase number, ex: 21'
SEARCH_SAFETY_PHRASE = u'start typing the phrase number, ex: 21'
SEARCH_HAZARD_STATEMENT = u'start typing the phrase number, ex: H310'
SEARCH_PRECAUTIONARY_STATEMENT = u'start typing the phrase number, ex: P102'
SEARCH_BORROW = u'the products I have borrowed'
SEARCH_BORROW_ENTITY = u'products borrowed in my entities'
SEARCH_BOOKMARK = u'bookmarked products'

SEARCH_COMMENT_CAS_NUMBER = u'enter an exact CAS number'
SEARCH_COMMENT_CE_NUMBER = u'enter an exact CE number'
SEARCH_COMMENT_NAME = u'enter a part of the product name or synonym'
SEARCH_COMMENT_EXACT_COC = u'product belongs exactly to the selected class(es) of compounds'
SEARCH_COMMENT_INCLUDE_CHILDREN_STORE_LOCATION = u'include children store locations'
SEARCH_ENTITY_NAME = u'entity name'
SEARCH_ENTITY_MEMBER = u'member'

DELETE_ARCHIVE_FOR_REQUEST = u'delete archived storage cards for the products of the current request'
PREVIEW_ARCHIVE_FOR_REQUEST = u'preview archived storage cards for the products of the current request'

