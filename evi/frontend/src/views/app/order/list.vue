<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'List'" :folder="'Order'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Add-Cart"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Orders</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.orders.length }}</p>
          </div>
        </b-card>
      </b-col>
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Calendar"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Date</p>
            <p class="text-primary text-24 line-height-1 mb-2"><nobr>{{ this.date }}</nobr></p>
          </div>
        </b-card>
      </b-col>
    </b-row>
    <div class="row">
      <div class="col-md-12">
        <div class="card mb-30">
          <div class="card-body p-0 mb-3">
            <b-row class="ml-3">
              <i class="nav-icon i-Add mt-3" style="font-size: 20px" v-b-toggle.collapse-e></i>
              <h5 class="card-title border-bottom p-3 mb-2">New Order</h5>
            </b-row>
            <b-collapse id="collapse-e" class="mt-3">
              <b-form>
                <b-row class="ml-3 mr-3">
                  <b-col md="12" class="mt-3">
                    <b-form-input id="input-1" v-model="ONumber" type="text" required placeholder="Order Number" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="mt-3 ml-3 mr-3">
                  <b-col md="4">
                    <b-form-datepicker  id="date-1" v-model="DatOrder" type="text" placeholder="Order Date" ></b-form-datepicker >
                  </b-col>
                  <b-col md="4">
                    <b-form-datepicker  id="date-2" v-model="DatDelivery" type="text" placeholder="Delivery Date" ></b-form-datepicker >
                  </b-col>
                  <b-col md="4">
                    <b-form-select id="input-2" v-model="OType" type="text" placeholder="Order Type" :options="optionsType"></b-form-select>
                  </b-col>
                </b-row>
                <b-row class="mt-3 ml-3 mr-3">
                  <b-col md="3">
                    <b-form-input id="input-3" v-model="CNumber" type="text" placeholder="Charge Number" ></b-form-input>
                  </b-col>
                  <b-col md="3">
                    <b-form-select id="input-4" v-model="DelStatus" :options="optionsStatus"></b-form-select>
                  </b-col>
                  <b-col md="6">
                    <b-form-select  id="select-1" v-model="Supplier" :options="optionsSupplier" value-field="id" text-field="txtSupplierName"></b-form-select>
                  </b-col>
                </b-row>
                <b-row class="mt-3 ml-3 mr-3">
                  <b-col md="6">
                    <b-button @click="emptyInput" block variant="outline-primary">Delete Input</b-button>
                  </b-col>
                  <b-col md="6">
                    <b-button @click="addOrder" block variant="primary">Add Order</b-button>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3">
                  <b-col md="12" class="mt-3">
                    <b-alert v-if="error" show variant="alert alert-card alert-danger" dismissible>
                      <strong class="text-capitalize">Error!</strong> The Input is not valid.
                    </b-alert>
                  </b-col>
                </b-row>
              </b-form>
            </b-collapse>
          </div>
        </div>
      </div>
    </div>
    <div class="row">
      <div class="col-md-12">
        <div class="card mb-30">
          <div class="card-body p-0">
            <AgGridVue class="ag-theme-alpine"
                id="gridOrders"
                :defaultColDef="defaultColDef"
                :columnDefs="columnDefs"
                :rowSelection="rowSelection"
                :rowData="rowData"
                :gridOptions="gridOptions"
                :suppressRowClickSelection="true"
                @grid-ready="onGridReady"
                @cellValueChanged="cellValueChanged"
                @row-selected="onRowSelected"
                :masterDetail="true"
                :detailCellRendererParams="detailCellRendererParams"
                :pagination="true"
                :paginationPageSize="10"
                :domLayout="domLayout"
                :modules="modules">
            </AgGridVue>
          </div>
        </div>
      </div>
    </div>
    <b-collapse v-model="show" class="ml-1 mr-3">
      <b-button @click="openModal" variant="primary">Delete Item</b-button>
    </b-collapse>
  </div>
  <!-- ============ Body content End ============= -->
</template>
<script>
import { apiService } from "@/common/api.service.js";
import { AgGridVue } from '@ag-grid-community/vue';
import { ClientSideRowModelModule } from "@ag-grid-community/client-side-row-model";
import { RichSelectModule } from '@ag-grid-enterprise/rich-select';
import { MenuModule } from '@ag-grid-enterprise/menu';
import { ColumnsToolPanelModule } from '@ag-grid-enterprise/column-tool-panel';
import { SetFilterModule } from '@ag-grid-enterprise/set-filter';
import { AllCommunityModules } from '@ag-grid-community/all-modules';
import { MasterDetailModule } from '@ag-grid-enterprise/master-detail';

export default {
  metaInfo: {    
    title: "Order"
  },
  components: {
    AgGridVue
  },
  data() {
    return {
      gridOptions: null,
      gridApi: null,
      columnApi: null,
      columnDefs: null,
      columnDefsMod: null,
      rowData: null,
      rowDataMod: null,
      rowSelection: null,
      defaultColDef: null,
      frameworkComponents: null,
      detailCellRendererParams: null,
      domLayout: null,
      modules: [
        ClientSideRowModelModule,
        SetFilterModule,
        RichSelectModule,
        MenuModule,
        ColumnsToolPanelModule,
        MasterDetailModule,
      ],
      suppliers: [],
      orders: [],
      show: false,
      visible: false,
      ONumber: '',
      DatOrder: '',
      DatDelivery: '',
      OType: '',
      CNumber: '',
      DelStatus: '',
      Supplier: '',
      date: null,
      next: null,
      error: false,
      optionsSupplier: [],
      optionsType: [
        { value: 'Sample', text: 'Sample' },
        { value: 'Customer', text: 'Customer' },
      ],
      optionsStatus: [
        { value: 'Delivered', text: 'Delivered' },
        { value: 'Not Delivered', text: 'Not Delivered' },
      ],
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Order Number", field: "txtOrderNumber", filter: 'agTextColumnFilter', checkboxSelection: true,},
      {headerName: "Order Date", field: "datOrder", filter: 'agTextColumnFilter',},
      {headerName: "Delivery Date", field: "datDelivery", filter: 'agTextColumnFilter',},
      {headerName: "Order Type", field: "txtOrderType", filter: 'agTextColumnFilter', cellEditor: 'agRichSelectCellEditor', cellEditorParams: { cellHeight: 50, values: ['Sample', 'Customer']}},
      {headerName: "Charge Number", field: "txtChargeNumber", filter: 'agTextColumnFilter',},
      {headerName: "Delivery Status", field: "txtDeliveryStatus", filter: 'agTextColumnFilter', cellEditor: 'agRichSelectCellEditor', cellEditorParams: { cellHeight: 50, values: ['Delivered', 'Not Delivered']}},
      {headerName: "Supplier", field: "idSupplier.txtSupplierName", filter: 'agTextColumnFilter', editable: false},
    ],
    this.defaultColDef = {
      flex: 1,
      editable: true,
      resizable: true,
      sortable: true,
      filter: true,
      floatingFilter: true,
    };
    this.rowSelection = 'single';
    this.domLayout = 'autoHeight';
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
  },
  methods: {
    async cellValueChanged(event) {     
      let endpoint = `/api/order/${event.node.data.id}/`;
      try {
        await apiService(endpoint, "PATCH", { 
          txtOrderNumber: event.node.data.txtOrderNumber,
          datOrder: event.node.data.datOrder,
          datDelivery: event.node.data.datDelivery,
          txtOrderType: event.node.data.txtOrderType,
          txtChargeNumber: event.node.data.txtChargeNumber,
          txtDeliveryStatus: event.node.data.txtDeliveryStatus,
          // idSupplier: event.node.data.idSupplier,
        })
      }
      catch (err) {
        console.log(err)
      }
    },
    onRowSelected(event) {
      this.show = this.show ? false : true
    },
    onGridReady(params) { 
    },
    getOrder() {
      if (!this.error) {
        let endpoint = `/api/order-list/`;
        apiService(endpoint)
          .then(data => {
            this.orders.push(...data.results);
            this.rowData = this.orders
          })
      }
    },
    getSup() {
      if (!this.error) {
        let endpoint = `/api/supplier/`;
        apiService(endpoint)
          .then(data => {
            this.suppliers.push(...data.results);
            this.optionsSupplier = this.suppliers
          })
      }
    },
    addOrder() {
      if (this.ONumber) {
        let endpoint = `/api/order/`;
        apiService(endpoint, "POST", { 
          txtOrderNumber: this.ONumber,
          datOrder: this.DatOrder,
          datDelivery: this.DatDelivery,
          txtOrderType: this.OType,
          txtChargeNumber: this.CNumber,
          txtDeliveryStatus: this.DelStatus,
          idSupplier: this.Supplier
          })
          .then(data => {
            if (data != 'ERROR'){
              this.orders.unshift(data);
              this.emptyInput();
            } else {
              this.error = true;
            }
          })
        if (this.error) {
          this.error = false;
        }
        } else {
          this.error = true;
        }
    },
    openModal(params) {
      this.$bvModal
        .msgBoxConfirm("Are you sure you want to delete the selected Order?", {
          title: "Please Confirm",
          size: "sm",
          buttonSize: "sm",
          okVariant: "danger",
          okTitle: "YES",
          cancelTitle: "NO",
          footerClass: "p-2",
          hideHeaderClose: false,
          centered: true
        })
        .then(value => {
          if (value) {
            this.deleteOrder();
          }
        })
    },
    async deleteOrder() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/order/${selectedRows[0].id}/`;
      try {
        var index = this.orders.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.orders, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    emptyInput() {
      this.ONumber = '',
      this.datOrder = [],
      this.datDelivery = [],
      this.OType = [],
      this.CNumber = '',
      this.DelStatus = [],
      this.Supplier = '',

      this.$root.$emit('bv::toggle::collapse', 'collapse-e')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getSup();
    this.getOrder();
    this.getDateToday();
  },
};
</script>
<style>
  i:focus,
  input:focus,
  select:focus,
  textarea:focus,
  button:focus {
      outline: none;
  }
</style>
