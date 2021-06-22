# -*- coding: utf-8 -*-
# Part of Softhealer Technologies.
{
    "name" : "Request For Quotation-Portal",
    "author" : "Softhealer Technologies",
    "website": "https://www.softhealer.com",
    "support": "support@softhealer.com",
    "category": "purchases",
    "summary": " Manage Multiple RFQs Module, Vendor Change RFQ Price App, Manage Request For Quotation Price, Request For Quote Update Price, Automatic Backend Price Change Odoo, Client Change RFQ Price ,Supplier Change Quotation Price Odoo.",
    "description": """Nowadays in a competitive market, several vendors sell the same products and everyone has their own price so it will difficult to manage multiple RFQ's at a time even in odoo there is no kind of feature where you can manage multiple requests for quotations in a single list. Currently in odoo vendor can see a purchase order, the vendor can't able to see RFQ this module provides vendor to see RFQ, where the vendor can change the price from portal or website for RFQ's. You can sort by RFQ by newest, name & total. You can sort filter purchase orders by all, request for quotation & sent. You can communicate in RFQ chatter.""",
    "version":"13.0.7",
    "depends" : ["base","purchase","portal"],
    "application" : True,
    "data" : [
            'security/ir.model.access.csv',
            'views/portal_templates.xml',
            ],
    "images": ["static/description/background.png", ],
    "live_test_url": "https://youtu.be/fC170lmqIqU",
    "auto_install":False,
    "installable" : True,
    "price": 35,
    "currency": "EUR"
}
