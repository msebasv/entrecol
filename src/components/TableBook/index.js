import React from 'react'

import { Button, Select, MenuItem } from '@mui/material'

import {
  DataGrid,
  gridPaginatedVisibleSortedGridRowIdsSelector,
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
        <MenuItem value={20}>20</MenuItem>
        <MenuItem value={25}>25</MenuItem>
        <MenuItem value={50}>50</MenuItem>
        <MenuItem value={100}>100</MenuItem>
      </Select>
      <Button disabled={page <= 1} onClick={() => setPage(page - 1)}>
        Previous
      </Button>
      <Button onClick={() => setPage(page + 1)}>Next</Button>
    </div>
  )
}
const TableBook = (props) => {
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
    const book = rows.map((book)=>{
      return ({
        bookID: book.bookID,
        num_pages: book.num_pages,
        average_rating: book.average_rating,
        title: book.title,
        publication_date: book.publication_date,
        ratings_count: book.ratings_count,
        language_code: book.language_code,
        publisher: book.publisher,
        authors: book.authors        
      }
      )
    })
    return book
  }

  return (
    <div className="container-table">
      <DataGrid
        getRowId={(row) => row.bookID}
        rows={Rows()}
        columns={columns}
        rowsPerPageOptions={[10, 20, 30, 40, 50, 100]}
        components={{
          Toolbar: CustomToolbar,
          Pagination: Test,
        }}
        pagination
      />
    </div>
  )
}

export default TableBook
