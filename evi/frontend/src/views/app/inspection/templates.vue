<template>
  <!-- ============ Body content start ============= -->
  <div class="main-content">
    <breadcumb :page="'Templates'" :folder="'Inspection'" />
    <b-row>
      <!-- ICON BG -->
      <b-col lg="6" md="6" sm="12">
        <b-card
          class="card-icon-bg card-icon-bg-primary o-hidden mb-30 text-center"
        >
          <i class="i-File"></i>
          <div class="content">
            <p class="text-muted mt-2 mb-0">Templates</p>
            <p class="inline text-primary text-24 line-height-1 mb-2">{{ this.templates.length }}</p>
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
              <h5 class="card-title border-bottom p-3 mb-2">New Template</h5>
            </b-row>
            <b-collapse id="collapse-e" class="mt-3">
              <b-form>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="4">
                    <b-form-input id="input-1" v-model="TempName" type="text" required placeholder="Template Name" ></b-form-input>
                  </b-col>
                  <b-col md="4">
                    <b-form-select id="select-1" v-model="Type" :options="optionsType" required ></b-form-select>
                  </b-col>
                  <b-col md="4">
                    <b-form-select id="select-2" v-model="IType" :options="optionsItemTypes" @change="onChange($event)" required ></b-form-select>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3 mt-3" v-if="IType">
                  <b-col md="12">
                    <b-form-checkbox-group  id="select-3" v-model="selAtt" :options="optionsAttributes" multiple
                      value-field="id" text-field="txtNameAttribute"></b-form-checkbox-group>
                  </b-col>
                </b-row>
                <b-row class="ml-3 mr-3 mt-3">
                  <b-col md="6">
                    <b-button @click="emptyInput" block variant="outline-primary">Delete Input</b-button>
                  </b-col>
                  <b-col md="6">
                    <b-button @click="addTemplate" block variant="primary">Add Template</b-button>
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
      <b-button @click="createInspection" variant="primary" class="mr-4">Create New Inspection</b-button>
      <b-button @click="openModal" variant="outline-primary">Delete Template</b-button>
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
    title: "Template"
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
      columnDefsAtt: null,
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
      templates: [],
      attributes: [],
      typeAttributes: [],
      selAtt: [],
      show: false,
      visible: false,
      TempName: '',
      Type: '',
      IType: null,
      date: null,
      next: null,
      error: false,
      optionsItemTypes: [
        { value: 'Glass', text: 'Glass' },
        { value: 'Case', text: 'Case' },
        { value: 'Frame', text: 'Frame' },
      ],
      optionsType: [
        { value: 'MF', text: 'Mess & Funktionsprüfung' },
        { value: 'CH', text: 'Chemische Prüfung' },
        { value: 'PH', text: 'Physikalische Prüfung' },
        { value: 'CA', text: 'Case Prüfung' },
        { value: 'FR', text: 'Frame Prüfung' },
        { value: 'QS', text: 'Qualitätssicherungsprüfung' },
      ],
      optionsAttributes: [],
    };
  },
  beforeMount() {
    this.gridOptions = {};
    this.columnDefs = [
      {headerName: "Template Name", field: "txtInspectionTemplateName", filter: 'agTextColumnFilter', cellRenderer: 'agGroupCellRenderer', checkboxSelection: true,},
      {headerName: "Template Type", field: "txtInspectionTemplateType", filter: 'agTextColumnFilter', cellEditor: 'agRichSelectCellEditor', 
        cellEditorParams: { cellHeight: 50, values: ['MF', 'CH', 'PH', 'CA', 'FR', 'QS']}
      },
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
        paginationAutoPageSize: 20,
        columnDefs: [
          {headerName: "Item Type", field: "txtItemType",},
          {headerName: "Attribute Key", field: "txtKeyAttribute",},
          {headerName: "Attribute Name", field: "txtNameAttribute",},
          {headerName: "Default Value", field: "txtValueDefault",},
          {headerName: "Value Type", field: "txtValueType",},
          {headerName: "Measure Unit", field: "txtMeasureUnit",},
        ],
        defaultColDef: { 
          flex: 1,
          editable: true,
          resizable: true,
          },
      },
      getDetailRowData: params => {
        params.successCallback(params.data.idInspectionTemplateAttribute);
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
    onChange(event) {
      this.optionsAttributes = [];
      this.typeAttributes = [];
      let endpoint = `/api/inspection-template-attribute/`;
      apiService(endpoint)
        .then(data => {
          this.typeAttributes.push(...data.results);
          this.typeAttributes.forEach(el => el.txtItemType == event ? this.optionsAttributes.push(el) : null)
        })
    },

    autoSizeAll(skipHeader) {
      var allColumnIds = [];
      this.gridColumnApi.getAllColumns().forEach(function(column) {
        allColumnIds.push(column.colId);
      });
      this.gridColumnApi.autoSizeColumns(allColumnIds, skipHeader);
    },
    async cellValueChanged(event) {     
      let endpoint = `/api/inspection-template/${event.node.data.id}/`;
      try {
        await apiService(endpoint, "PATCH", { 
          txtInspectionTemplateName: event.node.data.txtInspectionTemplateName,
          txtInspectionTemplateType: event.node.data.txtInspectionTemplateType,
        })
      }
      catch (err) {
        console.log(err)
      }
    },
    onRowSelected(event) {
      this.show = this.show ? false : true
    },
    getTemplates() {
      if (!this.error) {
        let endpoint = `/api/inspection-template-list/`;
        apiService(endpoint)
          .then(data => {
            this.templates.push(...data.results);
            this.rowData = this.templates
          })
      }
    },
    getAttributes() {
      if (!this.error) {
        let endpoint = `/api/inspection-template-attribute/`;
        apiService(endpoint)
          .then(data => {
            this.attributes.push(...data.results);
            // this.optionsAttributes = this.attributes
          })
      }
    },
    addTemplate() {
      if (this.TempName) {
        let endpoint = `/api/inspection-template/`;
        apiService(endpoint, "POST", { 
          txtInspectionTemplateName: this.TempName,
          txtInspectionTemplateType: this.Type,
          idInspectionTemplateAttribute: this.selAtt,
          })
          .then(data => {
            if (data){
              this.templates.unshift(data)
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
        .msgBoxConfirm("Are you sure you want to delete the selected Template?", {
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
            this.deleteTemplate();
          }
        })
    },
    async deleteTemplate() {
      var selectedRows = this.gridApi.getSelectedRows();
      let endpoint = `/api/inspection-template/${selectedRows[0].id}/`;
      try {
        var index = this.items.map(function(e) { return e.id; }).indexOf(selectedRows[0].id);
        this.$delete(this.templates, index)
        await apiService(endpoint, "DELETE")
        this.show = this.show ? false : true
      }
      catch (err) {
        console.log(err)
      }
    },
    createInspection() {
      var selectedRows = this.gridApi.getSelectedRows();
      localStorage.setItem('ITempID', selectedRows[0].id)
      this.$router.push('inspection')
    },
    deleteTempId() {
      localStorage.removeItem('ITempID')
    },
    emptyInput() {
      this.TempName = '',
      this.Type = null,
      this.IType = null,
      this.selAtt = null,
      this.$root.$emit('bv::toggle::collapse', 'collapse-o')
    },
    getDateToday() {
      var today = new Date();
      this.date = today.getDate()+' / '+(today.getMonth()+1)+' / '+today.getFullYear();
    },
  },
  created() {
    this.getTemplates();
    this.getAttributes();
    this.getDateToday();
    this.deleteTempId();
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
