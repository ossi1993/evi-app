<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'List'" :folder="'Supplier'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Truck"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Supplier</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.suppliers.length }}</p>
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
              <h5 class="card-title border-bottom p-3 mb-2">New Supplier</h5>
            </b-row>
            <b-collapse id="collapse-e" class="mt-3">
              <b-form>
                <b-row class="ml-3 mr-3">
                  <b-col md="12" class="mt-3">
                    <b-form-input id="input-1" v-model="SName" type="text" required placeholder="Supplier Name" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3">
                  <b-col md="4" class="mt-3">
                    <b-form-input id="input-2" v-model="Street1" type="text" placeholder="Street 1" ></b-form-input>
                  </b-col>
                  <b-col md="4" class="mt-3">
                    <b-form-input id="input-3" v-model="Street2" type="text" placeholder="Street 2" ></b-form-input>
                  </b-col>
                  <b-col md="4" class="mt-3">
                    <b-form-input id="input-4" v-model="Street3" type="text" placeholder="Street 3" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3">
                  <b-col md="2" class="mt-3">
                    <b-form-input id="input-5" v-model="Zip" type="text" placeholder="ZIP" ></b-form-input>
                  </b-col>
                  <b-col md="2" class="mt-3">
                    <b-form-input id="input-6" v-model="City" type="text" placeholder="City" ></b-form-input>
                  </b-col>
                  <b-col md="4" class="mt-3">
                    <b-form-input id="input-7" v-model="Province" type="text" placeholder="Province" ></b-form-input>
                  </b-col>
                  <b-col md="4" class="mt-3">
                    <b-form-input id="input-8" v-model="Land" type="text" required placeholder="Land" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3">
                  <b-col md="3" class="mt-3">
                    <b-form-input id="input-9" v-model="CPerson" type="text" placeholder="Contact Person" ></b-form-input>
                  </b-col>
                  <b-col md="3" class="mt-3">
                    <b-form-input id="input-10" v-model="Phone" type="text" placeholder="Phone" ></b-form-input>
                  </b-col>
                  <b-col md="3" class="mt-3">
                    <b-form-input id="input-11" v-model="Mail" type="text" placeholder="E-Mail" ></b-form-input>
                  </b-col>
                  <b-col md="3" class="mt-3">
                    <b-form-input id="input-12" v-model="Skype" type="text" placeholder="Skype" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3">
                  <b-col md="6" class="mt-3">
                    <b-button @click="emptyInput" block variant="outline-primary">Delete Input</b-button>
                  </b-col>
                  <b-col md="6" class="mt-3">
                    <b-button @click="addSup" block variant="primary">Add Supplier</b-button>
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
                id="gridSupplier"
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
      <b-button @click="openModal" variant="primary">Delete Supplier</b-button>
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
    title: "Supplier"
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
      show: false,
      visible: false,
      SName: '',
      Street1: '',
      Street2: '',
      Street3: '',
      Zip: '',
      City: '',
      Province: '',
      Land: '',
      CPerson: '',
      Phone: '',
      Mail: '',
      Skype: '',
      date: null,
      next: null,
      error: false,
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Supplier Name", field: "txtSupplierName", filter: 'agTextColumnFilter', checkboxSelection: true,},
      {headerName: "Street 1", field: "txtStreet1", filter: 'agTextColumnFilter',},
      {headerName: "Street 2", field: "txtStreet2", filter: 'agTextColumnFilter',},
      {headerName: "Street 3", field: "txtStreet3", filter: 'agTextColumnFilter',},
      {headerName: "ZIP", field: "txtZip", filter: 'agTextColumnFilter',},
      {headerName: "City", field: "txtCity", filter: 'agTextColumnFilter',},
      {headerName: "Province", field: "txtProvince", filter: 'agTextColumnFilter',},
      {headerName: "Land", field: "txtLand", filter: 'agTextColumnFilter',},
      {headerName: "Contact Person", field: "txtContactPerson", filter: 'agTextColumnFilter',},
      {headerName: "Phone", field: "txtCpPhone", filter: 'agTextColumnFilter',},
      {headerName: "E-Mail", field: "txtCpMail", filter: 'agTextColumnFilter',},
      {headerName: "Skype", field: "txtCpSkype", filter: 'agTextColumnFilter',},
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
      let endpoint = `/api/supplier/${event.node.data.id}/`;
      try {
        await apiService(endpoint, "PATCH", { 
          txtSupplierName: event.node.data.txtSupplierName,
          txtStreet1: event.node.data.txtStreet1,
          txtStreet2: event.node.data.txtStreet2,
          txtStreet3: event.node.data.txtStreet3,
          txtZip: event.node.data.txtZip,
          txtCity: event.node.data.txtCity,
          txtProvince: event.node.data.txtProvince,
          txtLand: event.node.data.txtLand,
          txtContactPerson: event.node.data.txtContactPerson,
          txtCpPhone: event.node.data.txtCpPhone,
          txtCpMail: event.node.data.txtCpMail,
          txtCpSkype: event.node.data.txtCpSkype,
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
    getSup() {
      if (!this.error) {
        let endpoint = `/api/supplier/`;
        apiService(endpoint)
          .then(data => {
            this.suppliers.push(...data.results);
            this.rowData = this.suppliers
          })
      }
    },
    addSup() {
      if (this.SName) {
        let endpoint = `/api/supplier/`;
        apiService(endpoint, "POST", { 
          txtSupplierName: this.SName,
          txtStreet1: this.Street1,
          txtStreet2: this.Street2,
          txtStreet3: this.Street3,
          txtZip: this.Zip,
          txtCity: this.City,
          txtProvince: this.Province,
          txtLand: this.Land,
          txtContactPerson: this.CPerson,
          txtCpPhone: this.Phone,
          txtCpMail: this.Mail,
          txtCpSkype: this.Skype
          })
          .then(data => {
            if (data){
              this.suppliers.unshift(data)
            } else {
              this.error = true;
            }
          })
        this.emptyInput()
        if (this.error) {
          this.error = false;
        }
        } else {
          this.error = true;
        }
    },
    openModal(params) {
      this.$bvModal
        .msgBoxConfirm("Are you sure you want to delete the selected Supplier?", {
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
            this.deleteSup();
          }
        })
    },
    async deleteSup() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/supplier/${selectedRows[0].id}/`;
      try {
        var index = this.suppliers.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.suppliers, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    emptyInput() {
      this.SName = '',
      this.Street1 = '',
      this.Street2 = '',
      this.Street3 = '',
      this.Zip = '',
      this.City = '',
      this.Province = '',
      this.Land = '',
      this.CPerson = '',
      this.Phone = '',
      this.Mail = '',
      this.Skype = ''

      this.$root.$emit('bv::toggle::collapse', 'collapse-o')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getSup();
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
