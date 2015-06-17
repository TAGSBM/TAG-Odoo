from openerp.osv import fields, osv

class tag_trident_custom_opportunity(osv.osv):

  _inherit = "crm.lead"

  _columns = {
    'TagCust1': fields.char('Data Upload ID', size=15),
    'TagCust2': fields.char('Business Type', size=25), 
    'TagCust3': fields.text('Accountant Name', size=50),
    'TagCust4': fields.text('Accountant Address', size=100), 
    'TagCust5': fields.text('Accountant contact details', size=100), 
    'TagCust6': fields.text('Company Name & or Trust Name', size=100), 
    'TagCust7': fields.char('Company ACN', size=25), 
    'TagCust8': fields.char('Company ABN', size=25),
    'TagCust9': fields.text('Name of Company Directors', size=100), 
    'TagCust10': fields.text('Directors Date of Birth', size=50), 
    'TagCust11': fields.char('Directors drivers licence details', size=100), 
    'TagCust12': fields.char('Website', size=50),
    'TagCust13': fields.char('Other 13', size=25),
    'TagCust14': fields.date('Settlement'), 
    'TagCust15': fields.float('Loan Term'), 
    'TagCust16': fields.char('Make',size=25), 
    'TagCust17': fields.char('Model', size=25), 
    'TagCust18': fields.char('Year', size=5),
    'TagCust19': fields.char('Color', size=25), 
    'TagCust20': fields.char('Reg No', size=25),
    'TagCust21': fields.char('Reg Expiry', size=25),
    'TagCust22': fields.char('Tyres %', size=25), 
    'TagCust23': fields.char('Kms', size=25), 
    'TagCust24': fields.selection([('unl','Unleaded'), ('ga','Gas'), ('die','Diesel'),('ele','Electric')],'Fuel Type'),
    'TagCust25': fields.selection([('man','Manual'), ('aut','Auto')], 'Trans'),
    'TagCust26': fields.selection([('1','4x4'), ('2','2x4'),('3','AWD')], 'X Drive'),
    'TagCust27': fields.char('Seating', size=25), 
    'TagCust28': fields.text('Other', size=200), 
    'TagCust29': fields.char('Job Description', size=25), 
    'TagCust30': fields.char('D.O.B', size=25),
    'TagCust31': fields.char('VIN', size=25),
    'TagCust32': fields.char('Engine Number', size=25), 
    'TagCust33': fields.char('Other 33', size=25),
    'TagCust34': fields.char('Make', size=30), 
    'TagCust35': fields.char('Model', size=30),
    'TagCust36': fields.char('Year', size=25),
    'TagCust37': fields.char('Color', size=25), 
    'TagCust38': fields.char('Reg No', size=25), 
    'TagCust39': fields.char('Reg Expiry', size=25), 
    'TagCust40': fields.char('Tyres %', size=25), 
    'TagCust41': fields.char('Kms', size=25),
    'TagCust42': fields.selection([('unl','Unleaded'), ('ga','Gas'), ('die','Diesel'),('ele','Electric')],'Fuel Type'), 
    'TagCust43': fields.selection([('man','Manual'), ('aut','Auto')], 'Trans'), 
    'TagCust44': fields.selection([('1','4x4'), ('2','2x4'),('3','AWD')], 'X Drive'), 
    'TagCust45': fields.char('Seating', size=25),
    'TagCust46': fields.text('Other', size=100),
    'TagCust47': fields.char('VIN', size=30), 
    'TagCust48': fields.char('Engine Number', size=30),
    'TagCust49': fields.char('Other 49', size=25), 
    'TagCust50': fields.char('Other 50', size=25),
    'TagCustL1Label': fields.char('Assetts', size=1),
    'TagCustAL1': fields.float('Cash at Bank'),
    'TagCustAL2': fields.float('Residential Property'), 
    'TagCustAL3': fields.float('Property 1'), 
    'TagCustAL4': fields.float('Property 2'), 
    'TagCustAL5': fields.float('Property 3'),
    'TagCustAL6': fields.float('Other Investments'),
    'TagCustAL7': fields.float('Fixtures & Fittings'), 
    'TagCustAL8': fields.float('Furniture'),
    'TagCustAL9': fields.float('Superannuation'), 
    'TagCustAL9a': fields.float('TDP Cover'),
    'TagCustAL9b': fields.float('Trauma'),
    'TagCustAL9c': fields.float('Income Protect'),
    'TagCustAL9d': fields.float('Life Ins'),
    'TagCustAL10': fields.float('Shares'),
    'TagCustAL11': fields.float('Plant & Equip'),
    'TagCustAL12': fields.float('Motor Vehicle'), 
    'TagCustAL13': fields.float('Bike/Van/Boat'), 
    'TagCustAL14': fields.float('Valuables'), 
    'TagCustAL15': fields.float('Business Val'),
    'TagCustAL16': fields.float('Total Assetts'),
    'TagCustL1Label2': fields.char('Liabilities', size=1),
    'TagCustAL21': fields.float('Overdraught'),
    'TagCustAL22': fields.float('Residential Property'), 
    'TagCustAL23': fields.float('Property 1'), 
    'TagCustAL24': fields.float('Property 2'), 
    'TagCustAL25': fields.float('Property 3'),
    'TagCustAL26': fields.float('Other Investments'),
    'TagCustAL27': fields.float('Credit Cards'), 
    'TagCustAL28': fields.float('Furniture'),
    'TagCustAL29': fields.float('Superannuation'), 
    'TagCustAL30': fields.float('Shares'),
    'TagCustAL31': fields.float('Plant & Equip'),
    'TagCustAL32': fields.float('Motor Vehicle'), 
    'TagCustAL33': fields.float('Bike/Van/Boat'), 
    'TagCustAL34': fields.float('Valuables'), 
    'TagCustAL35': fields.float('Business Val'),
    'TagCustAL36': fields.float('Total Liabilities'),
    'TagDevNotesFT1':fields.text('DFT1 Notes'),
    'TagDevNotesFT1H':fields.char('Help'),
    'TagDevNotesFT2':fields.text('FT2 Added for comments re development of this tab area'),
    'TagDevNotesFT3':fields.text('FT3 Added for comments re development of this tab area'),
    'TagDevNotesFT4':fields.text('FT4 Added for comments re development of this tab area'),
    'TagDevNotesFT5':fields.text('FT5 Added for comments re development of this tab area'),
    'TagDevNotesLT1':fields.text('LT1 Added for comments re development of this tab area'),
    'TagDevNotesLT2':fields.text('LT2 Added for comments re development of this tab area'),
    'TagDevNotesLT3':fields.text('LT3 Added for comments re development of this tab area'),
    'TagDevNotesLT4':fields.text('LT4 Added for comments re development of this tab area'),
    'TagDevNotesLT5':fields.text('LT5 Added for comments re development of this tab area'),
    'TagCustList01':fields.one2many('crm.lead.tag_cust_list_1', 'tag_list1_id', 'TagListA01'),
    'TagCustList02':fields.one2many('crm.lead.tag_cust_list_2', 'tag_list2_id', 'TagListA02'),
    'TagCustList03':fields.one2many('crm.lead.tag_cust_list_3', 'tag_list3_id', 'TagListA03'),
    'TagCustList04':fields.one2many('crm.lead.tag_cust_list_4', 'tag_list4_id', 'TagListA04'),
    'TagCustList05':fields.one2many('crm.lead.tag_cust_list_5', 'tag_list5_id', 'TagListA05')
  }
  
class tag_cust_list_1(osv.osv):

    _name = "crm.lead.tag_cust_list_1"
    
    _columns = {
        'tag_list1_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList101': fields.char('Name'),
        'TagList102': fields.char('Address'),
        'TagList103': fields.char('Phone'),
        'TagList104': fields.char('D.O.B'),
        'TagList105': fields.char('Lic No', size=20),
        'TagList106': fields.text('Note', size=150)
    }
    
class tag_cust_list_2(osv.osv):

    _name = "crm.lead.tag_cust_list_2"
    
    _columns = {
        'tag_list2_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),

        'TagList202': fields.char('Kms'),
        'TagList203': fields.char('L203'),
        'TagList204': fields.char('L204'),
        'TagList205': fields.char('L205'),
        'TagList206': fields.float('L206')
    }

class tag_cust_list_3(osv.osv):

    _name = "crm.lead.tag_cust_list_3"
    
    _columns = {
        'tag_list3_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList301': fields.char('Name'),
        'TagList302': fields.char('Address'),
        'TagList303': fields.char('Contact'),
        'TagList304': fields.char('Phone'),
        'TagList305': fields.char('Details'),
        'TagList305a': fields.char('Spotters'),
        'TagList306': fields.float('Price')
    }
    

class tag_cust_list_4(osv.osv):

    _name = "crm.lead.tag_cust_list_4"
    
    _columns = {
        'tag_list4_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList401': fields.char('Name'),
        'TagList402': fields.char('Address'),
        'TagList403': fields.char('Contact'),
        'TagList404': fields.char('Phone'),
        'TagList405': fields.text('Notes'),
        'TagList406': fields.char('Email'),
        'TagList407': fields.float('Price')
    }
    
class tag_cust_list_5(osv.osv):

    _name = "crm.lead.tag_cust_list_5"
    
    _columns = {
        'tag_list5_id': fields.many2one('crm.lead','Tag Back Reference Field', required=True, readonly=True),
        'TagList501': fields.char('Ref No'),
        'TagList502': fields.char('Term'),
        'TagList503': fields.char('Rate %'),
        'TagList504': fields.char('Broker'),
        'TagList505': fields.char('Trident Fee'),
        'TagList506': fields.char('Lender Fee'),
        'TagList507': fields.char('Lender Name')
    }
