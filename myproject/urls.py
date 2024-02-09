"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from app import views as main_views
from django.contrib.auth.views import LoginView, LogoutView
from vendor.additem import views as additem_views
from vendor.displayitem import views as displayitem_views
from vendor.updateitem import views as updateitem_views
from vendor.deleteitem import views as deleteitem_views
from vendor.confirmOrder import views as confirmorder_views
from vendor.updateOrderStatus import views as updateOrderStatus_views
from vendor.displayOrderHistory import views as displayOrderHistory_views
from vendor.displayRevenue import views as displayRevenue_views
from systemmanager.viewcustomer import views as viewcustomer_views
from systemmanager.viewvendor import views as viewvendor_views
from systemmanager.viewdeliveryperson import views as viewdeliveryperson_views
from systemmanager.viewsalesreport import views as viewsalesreport_views
from customer.browsemenu import views as browsemenu_views
from customer.addtocart import views as addtocart_views
from customer.paymentandcheckout import views as paymentandcheckout_views
from customer.vieworderstatus import views as vieworderstatus_views
from customer.vieworderhistory import views as vieworderhistory_views
from customer.viewtotalspent import views as  viewtotalspent_views


admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),

    re_path(r'^$', main_views.home, name='home'),
    re_path(r'^contact$', main_views.contact, name='contact'),
    re_path(r'^about$', main_views.about, name='about'),
    re_path(r'^login/$',
        LoginView.as_view(template_name = 'app/login.html'),
        name='login'),
    re_path(r'^logout$',
        LogoutView.as_view(template_name = 'app/index.html', next_page='home'),
        name='logout'),
    re_path(r'^menu$', main_views.menu, name='menu'),
    
    # vendor
    # update menu
    re_path(r'^displayitem$', displayitem_views.display_all_items, name='displayitem'),
    re_path(r'^additemform$', additem_views.additemform, name='additem_form'),
    re_path(r'^additemconfirmation$', additem_views.additemconfirmation, name='additem_confirmation'),
    re_path(r'^updateitemform$', updateitem_views.updateitemform, name='updateitem_form'),
    re_path(r'^updateitemconfirmation$', updateitem_views.updateitemconfirmation, name='updateitem_confirmation'),
    re_path(r'^deleteitemform$', deleteitem_views.deleteitem_form, name='deleteitemform'),
    re_path(r'^deleteitemconfirmation$', deleteitem_views.deleteitem_confirmation, name='deleteitem_confirmation'),
    # view and confirm order
    re_path(r'^displayPendingOrder$', confirmorder_views.displayPendingOrder, name='displayPendingOrder'),
    re_path(r'^pendingOrderDetail$', confirmorder_views.displayOrderPendingDetail, name='pendingOrderDetail'),
    re_path(r'^acceptOrderForm$', confirmorder_views.acceptorder_form, name='acceptOrderForm'),
    re_path(r'^acceptOrderConfirmation$', confirmorder_views.acceptorder_confirmation, name='acceptOrderConfirmation'),
    re_path(r'^rejectOrderForm$', confirmorder_views.rejectorder_form, name='rejectOrderForm'),
    re_path(r'^rejectOrderConfirmation$', confirmorder_views.rejectorder_confirmation, name='rejectOrderConfirmation'),
    # update order status
    re_path(r'^displayPreparingOrder$', updateOrderStatus_views.displayPreparingOrder, name='displayPreparingOrder'),
    re_path(r'^orderPreparingDetail$', updateOrderStatus_views.displayOrderPreparingDetail, name='orderPreparingDetail'),
    re_path(r'^completeOrderForm$', updateOrderStatus_views.completeorder_form, name='completeOrderForm'),
    re_path(r'^completeOrderConfirmation$', updateOrderStatus_views.completeorder_confirmation, name='completeOrderConfirmation'),
    re_path(r'^cancelOrderForm$', updateOrderStatus_views.cancelorder_form, name='cancelOrderForm'),
    re_path(r'^cancelOrderConfirmation$', updateOrderStatus_views.cancelorder_confirmation, name='cancelOrderConfirmation'),
    # view order history
    re_path(r'^displayOrderHistory$', displayOrderHistory_views.displayOrderHistory, name='displayOrderHistory'),
    re_path(r'^orderHistoryDetail$', displayOrderHistory_views.displayOrderHistoryDetail, name='orderHistoryDetail'),
    # display revenue
    re_path(r'^displayRevenue$', displayRevenue_views.displayRevenue, name='displayRevenue'),
    re_path(r'revenueOrderDetail$', displayRevenue_views.displayRevenueOrderDetail, name='revenueOrderDetail'),

    # System Manager
    re_path(r'^viewcustomer', viewcustomer_views.viewAllCustomer, name='viewcustomer'),
    re_path(r'^viewvendor', viewvendor_views.viewAllVendor, name = 'viewvendor'),
    re_path(r'^viewdeliveryperson', viewdeliveryperson_views.viewAllDeliveryperson, name = 'viewdeliveryperson'),
    re_path(r'^viewsalesreport', viewsalesreport_views.viewSalesReport, name='viewsalesreport'),

    # Customer
    re_path(r'^browsemenu', browsemenu_views.browse_menu, name='browsemenu'),
    re_path(r'^addtocart', addtocart_views.add_to_cart, name='addtocart'),
    re_path(r'^paymentandcheckout', paymentandcheckout_views.checkout, name='checkout'),
    re_path(r'^vieworderstatus', vieworderstatus_views.view_order_status, name='vieworderstatus'),
    re_path(r'^vieworderhistory', vieworderhistory_views.view_order_history, name='vieworderhistory'),
    re_path(r'^viewtotalspent', viewtotalspent_views.view_total_spent, name='viewtotalspent'),
]
