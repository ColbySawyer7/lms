import {
  Create,
  Datagrid,
  Edit,
  EditButton,
  List,
  SimpleForm,
  TextField,
  TextInput,
  DateInput,
  DateField,
  FunctionField
} from "react-admin";

import CheckoutButton from "../components/CheckoutButton";


interface BookRecord {
  id: number;
  title: string;
}

export const BookList = (props: any) => (
  <List {...props} filters={[]}>
    <Datagrid>
      <TextField source="title" />
      <TextField source="author" />
      <TextField source="isbn" />
      <DateField source="publication_date" />
      <TextField source="genre" />
      <FunctionField render={(record: BookRecord) => (
        <CheckoutButton book={record.id} />
      )} />
      <EditButton />
    </Datagrid>
  </List>
);

export const BookEdit = (props: any) => (
  <Edit {...props}>
    <SimpleForm>
      <TextInput source="title" />
      <TextInput source="author" />
      <TextInput source="isbn" />
      <DateInput source="publication_date" />
      <TextInput source="genre" />
    </SimpleForm>
  </Edit>
);

export const BookCreate = (props: any) => (
  <Create {...props}>
    <SimpleForm>
      <TextInput source="title" />
      <TextInput source="author" />
      <TextInput source="isbn" />
      <DateInput source="publication_date" />
      <TextInput source="genre" />
    </SimpleForm>
  </Create>
);
