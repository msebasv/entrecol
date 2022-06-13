import React, { useState } from 'react'

import { Button, Select, MenuItem } from '@mui/material'

import {
  DataGrid,
  gridPaginatedVisibleSortedGridRowIdsSelector,
  GridToolbar,
  GridToolbarContainer,
  useGridApiContext,
} from '@mui/x-data-grid'

import './index.css'

const getRowsFromCurrentPage = ({ apiRef }) =>
  gridPaginatedVisibleSortedGridRowIdsSelector(apiRef)

const CustomToolbar = () => {
  const apiRef = useGridApiContext()

  const handleExport = (options) => {
    apiRef.current.exportDataAsPrint(options)
  }

  return (
    <GridToolbarContainer>
      <Button
        onClick={() =>
          handleExport({ getRowsToExport: getRowsFromCurrentPage })
        }
      >
        Export PDF
      </Button>
    </GridToolbarContainer>
  )
}

function CustomPagination(props) {
  const { page, setPage, size, setSize } = props

  return (
    <div>
      <Select
        labelId="demo-simple-select-label"
        id="demo-simple-select"
        value={size}
        label="Rows"
        onChange={setSize}
      >
        <MenuItem value={5}>5</MenuItem>
        <MenuItem value={10}>10</MenuItem>
        <MenuItem value={15}>15</MenuItem>
      </Select>
      <Button disabled={page <= 0} onClick={() => setPage(page - 1)}>
        Previous
      </Button>
      <Button onClick={() => setPage(page + 1)}>Next</Button>
    </div>
  )
}
const TableMovie = (props) => {
  const { rows, columns, size, setSize, page, setPage } = props

  const Test = () => (
    <CustomPagination
      page={page}
      setPage={setPage}
      size={size}
      setSize={setSize}
    />
  )

  const Rows = () => {
    const mov = rows.map((movie)=>{
      return ({
        codigo: movie.codigo,
        nombre: movie.nombre,
        generos: movie.generos.map((gen) => gen.nombre)
        
      }
      )
    })
    return mov
  }

  return (
    <div className="container-table">
      <DataGrid
        getRowId={(row) => row.codigo}
        rows={Rows()}
        columns={columns}
        rowsPerPageOptions={[5, 10, 15]}
        components={{
          Toolbar: GridToolbar,
          Pagination: Test,
        }}
        pagination
      />
    </div>
  )
}

export default TableMovie
