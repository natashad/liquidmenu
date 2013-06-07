//php to convert menu tsv file to xml

$xmlWriter = new XMLWriter();
$xmlWriter->openUri('/var/www/wave-menu-helper/samkeenoodle.xml');
$xmlWriter->setIndent(true);
$xmlWriter->startDocument('1.0', 'UTF-8');
$xmlWriter->startElement('root');

$tsvFile = new SplFileObject('/var/www/wave-menu-helper/samkeenoodlemenu.tsv');
$tsvFile->setFlags(SplFileObject::READ_CSV);
$tsvFile->setCsvControl("\t");
foreach ($tsvFile as $line => $row) {
    if($line > 0) {
        $xmlWriter->startElement('menu-item');
        $xmlWriter->writeElement('number', $row[0]);
        $xmlWriter->writeElement('name', $row[1]);
        $xmlWriter->writeElement('price', $row[2]);
        $xmlWriter->endElement();
    }
}
$xmlWriter->endElement();
$xmlWriter->endDocument();