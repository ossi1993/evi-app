<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'Model List'" :folder="'Device'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Tag"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Models</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.models.length }}</p>
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
              <h5 class="card-title border-bottom p-3 mb-2">New Model</h5>
            </b-row>
            <b-collapse id="collapse-e" class="mt-3">
              <b-row class="ml-3 mt-3 mr-3">
                <b-col md="4">
                  <b-form-input id="input-1" v-model="MName" type="text" required placeholder="Model Name" ></b-form-input>
                </b-col>
                <b-col md="4">
                  <b-form-select  id="select-1" v-model="Manufacturer" :options="optionsManufacturer" required value-field="id" text-field="txtManufacturerName"></b-form-select>
                </b-col>
                <b-col md="4">
                  <b-form-select  id="select-2" v-model="Supplier" :options="optionsSupplier" required value-field="id" text-field="txtSupplierName"></b-form-select>
                </b-col>
              </b-row>
              <b-row class="ml-3 mt-3 mr-3">
                <b-col md="6">
                  <b-button @click="emptyInput" block variant="outline-primary">Delete Input</b-button>
                </b-col>
                <b-col md="6">
                  <b-button @click="addModel" block variant="primary">Add Model</b-button>
                </b-col>
              </b-row>
              <b-row class="ml-3 mt-3 mr-3">
                <b-col md="12">
                  <b-alert v-if="error" show variant="alert alert-card alert-danger" dismissible>
                    <strong class="text-capitalize">Error!</strong> The Input is not valid.
                  </b-alert>
                </b-col>
              </b-row>
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
                id="gridModel"
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
      <b-button @click="openModal" variant="primary">Delete Model</b-button>
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
    title: "Model"
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
      manufacturers: [],
      models: [],
      show: false,
      visible: false,
      MName: '',
      Manufacturer: '',
      Supplier: '',
      date: null,
      next: null,
      error: false,
      optionsSupplier: [],
      optionsManufacturer: [],
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Model Name", field: "txtModelName", filter: 'agTextColumnFilter', checkboxSelection: true,},
      {headerName: "Manufacturer", field: "idManufacturer.txtManufacturerName", filter: 'agTextColumnFilter', editable: false},
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
      let endpoint = `/api/model/${event.node.data.id}/`;
      console.log(event.node.data.id)
      try {
        await apiService(endpoint, "PATCH", { 
          txtModelName: event.node.data.txtModelName,
          // idManufacturer: event.node.data.idManufacturer,
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
      // this.autoSizeAll(false);
    },
    getManufacturer() {
      if (!this.error) {
        let endpoint = `/api/manufacturer/`;
        apiService(endpoint)
          .then(data => {
            this.manufacturers.push(...data.results);
            this.optionsManufacturer = this.manufacturers
          })
      }
    },
    getSupplier() {
      if (!this.error) {
        let endpoint = `/api/supplier/`;
        apiService(endpoint)
          .then(data => {
            this.suppliers.push(...data.results);
            this.optionsSupplier = this.suppliers
          })
      }
    },
    getModels() {
      if (!this.error) {
        let endpoint = `/api/model-list/`;
        apiService(endpoint)
          .then(data => {
            this.models.push(...data.results);
            this.rowData = this.models
          })
      }
    },
    addModel() {
      if (this.MName) {
        let endpoint = `/api/model/`;
        apiService(endpoint, "POST", { 
          txtModelName: this.MName,
          idManufacturer: this.Manufacturer,
          idSupplier: this.Supplier,
          })
          .then(data => {
            if (data) {
              console.log(data)
              this.models.unshift(data)
            } else {
              this.error = true;
            }
          })
        this.emptyInput();
        if (this.error) {
          this.error = false;
        }
        } else {
          this.error = true;
        }
    },
    openModal(params) {
      this.$bvModal
        .msgBoxConfirm("Are you sure you want to delete the selected Model?", {
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
            this.deleteModel();
          }
        })
    },
    async deleteModel() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/model/${selectedRows[0].id}/`;
      try {
        var index = this.models.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.models, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    emptyInput() {
      this.MName = '',
      this.Manufacturer = [],
      this.Supplier = [],

      this.$root.$emit('bv::toggle::collapse', 'collapse-e')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getManufacturer();
    this.getSupplier();
    this.getModels();
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
