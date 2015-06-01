from openerp.osv import fields,osv
from openerp import tools,api, exceptions,models

class usr(osv.Model):
    _name = 'usr'
 
    _columns = {
    'name' : fields.char(string="name", required=True),
    'email' : fields.char(string="email", required=True) ,
    'department'  : fields.char(string="department", required=True) ,
    'position' : fields.char(string="position", required=True),
    'department_id': fields.many2one('hr.department', 'Department'),
}
    def create(self, cr, uid, vals, context=None):
        user_obj = self.pool.get('res.users')
        hr_obj = self.pool.get('hr.employee')

        vals_user = {
            'name': vals.get('name'),
            'login': vals.get('email'),
            'password' : "12345",
            #other required field 
        }
        vals_hr = {
            'name': vals.get('name'),
            
            #other required field 
        }
        user_obj.create(cr, uid, vals_user, context)
        hr_obj.create(cr, uid, vals_hr, context)
        
        result = super(usr, self).create(cr, uid, vals, context=context)
        
        return result
