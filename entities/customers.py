
def customers_entities(db, orm):
    class Customer(db.Entity):
        __table__ = 'customers'


        first_name = orm.Optional(str, 40)
        last_name = orm.Optional(str, 40)
        age = orm.Optional(int)
        sex = orm.Optional(str, 40)
        vehicle_make= orm.Optional(str, 40)
        vehicle_model= orm.Optional(str, 40)
        vehicle_year= orm.Optional(str, 40)
        vehicle_type= orm.Optional(str, 40)
        iban= orm.Optional(str, 50)
        credit_card_number= orm.Optional(str, 50)
        credit_card_security_code= orm.Optional(str, 5)
        credit_card_start_date= orm.Optional(str, 20)
        credit_card_end_date= orm.Optional(str, 20)
        address_main= orm.Optional(str, 50)
        address_city= orm.Optional(str, 50)
        address_postcode = orm.Optional(str, 20)
        retired= orm.Optional(str,10)
        dependants= orm.Optional(str, 10)
        marital_status= orm.Optional(str, 30)
        salary= orm.Optional(str, 20)
        pension= orm.Optional(str, 20)
        company= orm.Optional(str, 50)
        commute_distance= orm.Optional(str, 20)
        # address_postcode= orm.Optional(str,20)
        def __str__(self):
            return self.first_name, self.last_name

    return Customer