<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'List'" :folder="'Item'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-Eci-Icon"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Items</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.items.length }}</p>
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
              <h5 class="card-title border-bottom p-3 mb-2">New Item</h5>
            </b-row>
            <b-collapse id="collapse-e" class="mt-3">
              <b-form>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="3">
                    <b-form-input id="input-1" v-model="ArtNum" type="text" required placeholder="Article Number" ></b-form-input>
                  </b-col>
                  <b-col md="3">
                    <b-form-input id="input-2" v-model="Description" type="text" required placeholder="Item Description" ></b-form-input>
                  </b-col>
                  <b-col md="3">
                    <v-select  id="select-1" v-model="Type" :options="optionsType" required placeholder="Choose Item Type" :reduce="Type => Type.code"></v-select>
                  </b-col>
                  <b-col md="3">
                    <b-form-input id="input-3" v-model="Version" type="text" required placeholder="Version" ></b-form-input>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="3">
                    <b-form-input id="input-4" v-model="Cost" type="text" placeholder="Cost" ></b-form-input>
                  </b-col>
                  <b-col md="3">
                    <b-form-input id="input-5" v-model="GtinEan" type="text" placeholder="GTIN / EAN" ></b-form-input>
                  </b-col>
                  <b-col md="3">
                    <v-select  id="select-2" v-model="Outline" :options="optionsOutline" required placeholder="Choose Outline" :reduce="Outline => Outline.code"></v-select>
                  </b-col>
                  <b-col md="3">
                    <!-- <v-select  id="select-3" label="txtModelName" v-model="selectedModels" :reduce="txtModelName => txtModelName.id"
                    code="id" :options="optionsModels" multiple placeholder="Choose Models"></v-select> -->
                    <b-form-select  id="select-3" v-model="selectedModels" :options="optionsModels" multiple value-field="id" text-field="txtModelName"></b-form-select>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="6">
                    <b-button @click="emptyInput" block variant="outline-primary">Delete Input</b-button>
                  </b-col>
                  <b-col md="6">
                    <b-button @click="addItem" block variant="primary">Add Item</b-button>
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
                id="gridItems"
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
    title: "Item"
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
      items: [],
      models: [],
      show: false,
      visible: false,
      selectedModels: [],
      ArtNum: '',
      Description: '',
      Type: '',
      Version: '',
      Cost: '',
      GtinEan: '',
      Outline:'',
      Link: '',
      date: null,
      next: null,
      error: false,
      optionsType: [
        { code: 'Glass', label: 'Glass' },
        { code: 'Case', label: 'Case' },
        { code: 'Frame', label: 'Frame' },
      ],
      optionsOutline: [
        { code: '2D', label: '2D' },
        { code: '3D', label: '3D' },
        { code: 'FC', label: 'Full Cover' },
      ],
      optionsModels: [],
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Article Number", field: "txtArticlenumber", filter: 'agTextColumnFilter', cellRenderer: 'agGroupCellRenderer', checkboxSelection: true,},
      {headerName: "Item Description", field: "txtDescription", filter: 'agTextColumnFilter', width: 300,},
      {
        headerName: "Type", field: "txtType", filter: 'agTextColumnFilter',
        editable: true, cellEditor: 'agRichSelectCellEditor', cellEditorParams: { cellHeight: 50, values: ['Glass', 'Case', 'Frame']}
      },
      {headerName: "Version", field: "txtVersion", filter: 'agTextColumnFilter',},
      {headerName: "Cost", field: "curCost", filter: 'agTextColumnFilter', hide: true,},
      {headerName: "GTIN / EAN", field: "txtGtinEan", filter: 'agTextColumnFilter',},
      {headerName: "Outline", field: "txtOutline", filter: 'agTextColumnFilter',},
      {headerName: "Link", field: "txtLink", filter: 'agTextColumnFilter', hide: true,},
    ],
    this.defaultColDef = {
      flex: 1,
      editable: true,
      resizable: true,
      sortable: true,
      filter: true,
      floatingFilter: true,
    };
    this.detailCellRendererParams = {
      detailGridOptions: {
        rowSelection: 'single',
        suppressRowClickSelection: true,
        enableRangeSelection: true,
        pagination: true,
        paginationAutoPageSize: true,
        columnDefs: [
          {
            field: 'txtModelName',
            headerName: 'Model Name'
          },
        ],
        defaultColDef: { 
          flex: 1,
          // editable: true,
          resizable: true,
          },
      },
      getDetailRowData: params => {
        params.successCallback(params.data.deviceModels);
      },
    }
    this.rowSelection = 'single';
    this.domLayout = 'autoHeight';
  },
  mounted() {
    this.gridApi = this.gridOptions.api;
    this.gridColumnApi = this.gridOptions.columnApi;
  },
  methods: {
    async cellValueChanged(event) {     
      let endpoint = `/api/item/${event.node.data.id}/`;
      console.log(event.node.data.id)
      try {
        await apiService(endpoint, "PATCH", { 
          txtArticlenumber: event.node.data.txtArticlenumber,
          txtDescription: event.node.data.txtDescription,
          txtType: event.node.data.txtType,
          txtVersion: event.node.data.txtVersion,
          curCost: event.node.data.curCost,
          txtGtinEan: event.node.data.txtGtinEan,
          txtOutline: event.node.data.txtOutline,
          txtLink: event.node.data.txtLink,
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
    getItems() {
      if (!this.error) {
        let endpoint = `/api/item-list/`;
        apiService(endpoint)
          .then(data => {
            this.items.push(...data.results);
            this.rowData = this.items
          })
      }
    },
    getDeviceModels() {
      if (!this.error) {
        let endpoint = `/api/model/`;
        apiService(endpoint)
          .then(data => {
            this.models.push(...data.results);
            this.optionsModels = this.models
          })
      }
    },
    addItem() {
      if (this.ArtNum) {
        let endpoint = `/api/item/`;
        console.log(typeof this.ArtNum)
        console.log(typeof this.Type)
        apiService(endpoint, "POST", { 
          txtArticlenumber: this.ArtNum,
          txtDescription: this.Description,
          txtType: this.Type,
          txtVersion: this.Version,
          curCost: this.Cost,
          txtGtinEan: this.GtinEan,
          txtOutline: this.Outline,
          txtLink: this.Link,
          deviceModels: this.selectedModels,
          })
          .then(data => {
            if (data != 'ERROR'){
              this.items.unshift(data)
              this.emptyInput()
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
        .msgBoxConfirm("Are you sure you want to delete the selected Item?", {
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
            this.deleteItem();
          }
        })
    },
    async deleteItem() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/item/${selectedRows[0].id}/`;
      try {
        var index = this.items.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.items, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    emptyInput() {
      this.ArtNum = '',
      this.Description = '',
      this.Type = [],
      this.Version = '',
      this.Cost = '',
      this.GtinEan = '',
      this.Outline = [],
      this.Link = '',
      this.selectedModels = [],

      this.$root.$emit('bv::toggle::collapse', 'collapse-e')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getItems();
    this.getDeviceModels();
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
