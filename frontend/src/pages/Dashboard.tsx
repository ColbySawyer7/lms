import React from 'react';
import Card from '@mui/material/Card';
import CardHeader from '@mui/material/CardHeader';
import CardContent from '@mui/material/CardContent';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import Box from '@mui/material/Box';
import { basePath } from '../providers/env';
import { useState, useEffect } from 'react';

const Component = () => {
  const [countBooks, setCountBooks] = useState(0);
  const [countMembers, setCountMembers] = useState(0);
  const [countTransactions, setCountTransactions] = useState(0);
  const [countLibraries, setCountLibraries] = useState(0);
  const countOverdueBooks = 5;  // This might also be fetched


  useEffect(() => {
    try{
    fetch(`${basePath}/api/v1/books/count`)
      .then(response => response.json())
      .then(data => setCountBooks(data));
    } catch (e) {
      console.error(e);
    }

    try{
      fetch(`${basePath}/api/v1/libraries/count`)
        .then(response => response.json())
        .then(data => setCountLibraries(data));
      } catch (e) {
        console.error(e);
      }  
    
    try{
    fetch(`${basePath}/api/v1/transactions/count`)
      .then(response => response.json())
      .then(data => setCountTransactions(data));
    } catch (e) {
      console.error(e);
    }

    try{
    fetch(`${basePath}/api/v1/members/count`)
      .then(response => response.json())
      .then(data => setCountMembers(data));
    } catch (e) {
      console.error(e);
    }
  }, []);
  
  return (
  <Card>
    <CardHeader title="Welcome to the Library Management System (LMS)" sx={{textAlign: "center"}}/>
    <CardContent>
      <Grid container spacing={2} justifyContent="space-around">
        <Grid item xs={3}>
          <CounterBox label="Total Books" count={countBooks} />
        </Grid>
        <Grid item xs={3}>
          <CounterBox label="Total Members" count={countMembers} />
        </Grid>
        <Grid item xs={3}>
          <CounterBox label="Available Libraries" count={countLibraries} />
        </Grid>
        <Grid item xs={3}>
          <CounterBox label="Books Loaned Out" count={countTransactions} />
        </Grid>
      </Grid>
    </CardContent>
  </Card>
);

}

interface CounterBoxProps {
  label: string;
  count: number;
}

const CounterBox: React.FC<CounterBoxProps> = ({ label, count }) => (
  <Box textAlign="center">
    <Typography variant="h4" color="primary">{count}</Typography>
    <Typography variant="subtitle1">{label}</Typography>
  </Box>
);
export default Component;
